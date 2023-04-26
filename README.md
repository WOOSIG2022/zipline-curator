# zipline-curator
# How to import local csv data

Step 1: Put the csv_data folder in a local directory, for example, "C://users/username/zipline_reloaded/data"

Step 2: Put the csv_data.py file in your data bundles directory. In my case, it is "C:\Programs\Anaconda\envs\zip38\Lib\site-package\zipline\data\bundles". Remember to change the path in the file to "C://users/username/zipline_reloaded/data"

Step 3: Put the extension.py file in your local directory "C://users/username/.zipline"

Step 4: In your anaconda terminal, run 
`from zipline.data.bundles import register, csv_data
register('csv_data', csv_data.csv_data, calendar_name = "NYSE")`

You will see error: `TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value`
