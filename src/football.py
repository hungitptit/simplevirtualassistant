from football_data_api import data_fetchers
data = data_fetchers.CompetitionData()
teams_in_premier = data.get_info('teams')
from datetime import datetime
date_today = datetime.today()
matches = data.get_info('matches', dateFrom='2019-12-10', dateTo=date_today)
print(matches)
