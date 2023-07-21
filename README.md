# zipline-curator
# How to import local csv data (minute)

Step 1: Put the csv file in a local directory, for example, "C://users/username/zipline_reloaded/data/minute"

Step 2: Put the extension.py file in your local directory "C://users/username/.zipline". Change the path to one level above your minute folder.

Step 3: In your anaconda terminal, run the code below to inject the data:
```
zipline ingest -b csv_data_minute
```
