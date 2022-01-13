import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import sys


def get_hrefs(datepat):
    '''
    Get a list of the hrefs available from mta turnstile data website
    Parameters
    ----------
    datepat : str
        string representing regex pattern for a date (e.g., '21.*')

    Returns
    -------
    list of hrefs
    '''
    # main page containing all the mta turnstile links
    url = 'http://web.mta.info/developers/'
    response = requests.get(url + 'turnstile.html')
    soup = BeautifulSoup(response.content, features="lxml")

    # links to weeks of turnstile data
    href_pat = re.compile(r'.*data.*turnstile_' + datepat)
    hrefs = soup.find_all('a', attrs={'href': href_pat})
    hrefs = [url + h.attrs['href'] for h in hrefs]

    # remove dates prior to 2015 (the MTA schema changed then)
    hrefs = [href for href in hrefs if href_to_week(href) > '2014-12-31']

    return hrefs


def href_to_week(href):
    week = href[href.find('turnstile_') + 10:href.find('.txt')]
    week = pd.to_datetime(week, yearfirst=True).strftime('%Y-%m-%d')
    return week


def load_week(href, con):
    '''
    Load one week of data into SQLite.
    '''
    week = href_to_week(href)

    print(f"Week: {week} -- Getting data ...")
    df = pd.read_csv(href)

    # strip whitespace from headers
    df.columns = df.columns.str.strip()

    # drop data into database
    print(f"Week: {week} -- Inserting into SQLite ...")
    df.to_sql("mta_data", con, if_exists='append', index=False)


if __name__ == '__main__':
    # regex for weeks to scrape
    if len(sys.argv) > 1:
        datepat = sys.argv[1]  # input
    else:
        datepat = pd.Timestamp.today().strftime('%y%m')  # default to this month

    hrefs = get_hrefs(datepat)

    # check for user confirmation
    weeks = [href_to_week(h) for h in hrefs]
    print(f"\n{len(weeks)} weeks to collect:\n")
    print(weeks)

    if input(f"\nContinue? (Y/n) ").lower() not in ['yes', 'y']:
        exit()

    # connect to (or create) mta_data SQLite database
    print("\nConnecting to (or creating) mta_data SQLite database ...\n")
    con = sqlite3.connect("mta_data.db")

    for href in hrefs:
        load_week(href, con)

    con.close()

    print("\nAll done!\n")