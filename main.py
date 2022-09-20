from pytrends.request import TrendReq
from datetime import datetime

#pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, requests_args={'verify':False})
pytrend = TrendReq()

trends = []

trendingtoday = pytrend.today_searches(pn='IN')
for i in trendingtoday[:5]:
    trends.append(i.split('=')[1][:-5].replace('+',' '))

with open('trend.csv','a') as file:
    file.writelines(f'{datetime.now().__str__()},{",".join(trends)}\n')