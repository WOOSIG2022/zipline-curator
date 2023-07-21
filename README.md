# zipline-curator
# How to import local csv data (daily)

Step 1: Put the csv_data folder in a local directory, for example, "C://users/username/zipline_reloaded/data"

Step 2: Put the csv_data.py file in your data bundles directory. In my case, it is "C:\Programs\Anaconda\envs\zip38\Lib\site-package\zipline\data\bundles". Remember to change the path in the file to "C://users/username/zipline_reloaded/data".

Step 3: Put the extension.py file in your local directory "C://users/username/.zipline".

Step 4: In your anaconda terminal, run the code below to inject the data:
```
zipline ingest -b csv_data
```


You may see error: 

`TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value`

To correct it, find file "bcolz_daily_bars.py" in your data directory such as "C:\Users\shopp\Anaconda3\envs\Py38\lib\site-packages\zipline\data\". Find function  winsorise_uint32 and change the code  `df[mask] = 0` to `# df[mask] = 0`. This function makes sure that any integer value not great than the program can process.

I.e., the number 4,294,967,295, equivalent to the hexadecimal value FFFF,FFFF16, is the maximum value for a 32-bit unsigned integer in computing.

But the number is much larger than what is our data.

Step 5: In your first zipline backtest notebook, change the symbol (e.g., from "AAPL" to "SHY"), change the dates
```# Set start and end date
start_date = pd.Timestamp('2018-06-05',tz ='utc')

end_date = pd.Timestamp('2020-3-16',tz ='utc')
```
and change the bundle name (`bundle='csv_data'`). 

You should be able to run the test correctly.


Python warnings during injection:

Warning 1.

```
C:\Users\shopp\Anaconda3\envs\Py38\lib\site-packages\zipline\assets\asset_writer.py:823: FutureWarning: iteritems is deprecated and will be removed in a future version. Use .items instead.
  for column, dtype in df.dtypes.iteritems():
```
To correct it, just go to the file and replace .iteritems() with .items().

Warning 2.

```
C:\Users\shopp\Anaconda3\envs\Py38\lib\site-packages\zipline\assets\asset_writer.py:827: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
```

I don't know how to correct this. According to this [post](https://stackoverflow.com/questions/71082494/getting-a-warning-when-using-a-pyodbc-connection-object-with-pandas), it is not an essential warning. So you can ignore it by adding this at the top of your file "extension.py:.

```
import warnings
warnings.filterwarnings("ignore")
```
