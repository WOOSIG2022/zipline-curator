# zipline-curator
# How to import local csv data

Step 1: Put the csv_data folder in a local directory, for example, "C://users/username/zipline_reloaded/data"

Step 2: Put the csv_data.py file in your data bundles directory. In my case, it is "C:\Programs\Anaconda\envs\zip38\Lib\site-package\zipline\data\bundles". Remember to change the path in the file to "C://users/username/zipline_reloaded/data"

Step 3: Put the extension.py file in your local directory "C://users/username/.zipline".

Step 4: In your anaconda terminal, run the code below:

```lang = python

from zipline.data.bundles import register, csv_data

register('csv_data', csv_data.csv_data, calendar_name = "NYSE")```

You may see error: 

`TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value`

To correct it, find file "bcolz_daily_bars.py" in your data directory such as "C:\Users\shopp\Anaconda3\envs\Py38\lib\site-packages\zipline\data\". Find function  winsorise_uint32 and change the code  `df[mask] = 0` to `# df[mask] = 0`. This function makes sure that any integer value not great than the program can process.

I.e., the number 4,294,967,295, equivalent to the hexadecimal value FFFF,FFFF16, is the maximum value for a 32-bit unsigned integer in computing.

Step 5: In your first zipline backtest notebook, change the symbol (e.g., from "AAPL" to "SHY"), change the dates (`# Set start and end date
start_date = pd.Timestamp('2018-06-05',tz ='utc')
end_date = pd.Timestamp('2020-3-16',tz ='utc')`) , and bundle name (`bundle='csv_data'`) 

You should be able to run the test correctly.
