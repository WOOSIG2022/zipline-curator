# zipline-curator

## Installing Zipline

conda install -c ml4t -c conda-forge -c ranaroussi zipline-reloaded

zipline ingest -b quandl

Quandl ingest 
Value error:

I manually edited in file "..\site-packages\zipline\data\bundles\quandl.py":
from # api_key = environ.get('QUANDL_API_KEY')
to  api_key = 'XXXXXXXXX'
then it's working.

Type error:
In \trading_calendars\calendar_helpers.py change
# orig NP_NAT = np.array([pd.NaT], dtype=np.int64)[0]
# ajjc old issue #40 2022-08-09
NP_NAT = np.array([pd.NaT.asm8.view('i8')], dtype=np.int64)[0]

Key error: "Turkey"
pip install iso3166==2.0.2

Type error:



Pyfolio

pip install pyfolio-reloaded
conda install -c ml4t pyfolio-reloaded
