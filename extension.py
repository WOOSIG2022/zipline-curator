import pandas as pd
from zipline.data.bundles.csvdir import csvdir_equities

import warnings
warnings.filterwarnings('ignore')

start_session = pd.Timestamp('2020-12-07', tz='utc')
end_session = pd.Timestamp('2020-12-15', tz='utc')

register(
 	'csv_data_minute',
 	csvdir_equities(
 		['minute'],
 		r'C:\Users\shopp\Box\WOOatUB\ZhenProjects\Zipline_TradingEvolved\data\csv_data', # Change it to the path one level above your minute folder
 		),
	
	
	calendar_name = 'NYSE', 
	start_session=start_session,
	end_session=end_session
	)
