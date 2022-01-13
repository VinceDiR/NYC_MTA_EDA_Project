# Using *get_mta.py*

### Step 1

Save the *get_mta.py* file wherever you'd like to put your SQLite database (it will be called **mta_data**).

### Step 2

In that directory, run

```
python get_mta.py "<pat>"
```

*(Notice the `"`s)* where `<pat>` is a [regex](https://www.computerhope.com/jargon/r/regex.htm) pattern representing the weeks you'd like to grab from the [mta website](http://web.mta.info/developers/turnstile.html). If you don't type any `<pat>`, and just run `python get_mta.py`, it will default to pull data from the current month. For example, to pull data from the year 2021 (`21`) in the month of May (`05`), you'd run

```
python get_mta.py "2105"
```

Possible `<pat>` strings:

* (default) the current month = `  `
* the 5th month of 2021 = `"2105"`
* a few select months = `"(2102|2103|2104|2105)"`
* all weeks from the year 2021 = `"21"`
* the 1st month of each year* = `"[0-9][0-9]01"`

**This last one will take a while ...*

### Step 3

Access the saved *mta_data.db* file, and start working on your project.

**Only run once! Otherwise, be careful!** If there is any intersection between runs, you will have duplicated data, and you'll have to delete the *mta_data.db* file, and start over.
