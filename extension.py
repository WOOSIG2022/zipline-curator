import pandas as pd
from zipline.data.bundles import register, csv_data

start_session = pd.Timestamp('2018-01-05', tz='utc')
end_session = pd.Timestamp('2020-07-31', tz='utc')
register(
	'csv_data', 
	csv_data.csv_data, 
	calendar_name = 'NYSE', 
	start_session=start_session,
	end_session=end_session
	)