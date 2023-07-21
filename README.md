# zipline-curator

## Installing Zipline-reloaded

`conda install -c ml4t -c conda-forge -c ranaroussi zipline-reloaded`

## Ingesting Quandl data

`zipline ingest -b quandl`

You may see a messsage starting with `ValueError:`. 

Then you need to manually edit in file "..\site-packages\zipline\data\bundles\quandl.py", from 

> api_key = environ.get('QUANDL_API_KEY')

to  

> api_key = '[your quandl api key]'

It should work.

If you see a message starting with `Type error:`, you need to manually edit in file "..\trading_calendars\calendar_helpers.py", from 

> orig NP_NAT = np.array([pd.NaT], dtype=np.int64)[0]

to
> NP_NAT = np.array([pd.NaT.asm8.view('i8')], dtype=np.int64)[0].



If you see a message with `Key error: "Turkey"`, you run this in the terminal
`pip install iso3166==2.0.2`.




## Installing Pyfolio

`pip install pyfolio-reloaded` or `conda install -c ml4t pyfolio-reloaded`
