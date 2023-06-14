import pandas as pd
from zipline.data.bundles import register, csv_NYSE, csvdir
start_session = pd.Timestamp('2020-12-07 09:30:00', tz='utc')
end_session = pd.Timestamp('2020-12-15 14:05:10', tz='utc')
register('csv_data',
		csv_NYSE.csv_NYSE(tframes=["minute"], csvdir="/Users/Akshit/PycharmProjects/woosig2022/zipline-curator/data/"),
		calendar_name = 'NYSE',
		start_session=start_session,
		end_session=end_session)
