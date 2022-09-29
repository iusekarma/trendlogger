from pytrends.request import TrendReq
from datetime import datetime

#get the top 5 thrends
pytrend = TrendReq()
trends = []
trendingtoday = pytrend.today_searches(pn='IN')
for i in trendingtoday[:5]:
    trends.append(i.split('=')[1][:-5].replace('+',' '))

#log it in trend.csv
with open('trend.csv','a') as file:
    file.writelines(f'{datetime.now().__str__()},{",".join(trends)}\n')

#Update readme for latest trends
readme = ''
with open('README.md','r') as file:
    readme = file.read()

first_section = readme[:readme.index('<!-- Last Trends -->')]
last_section =  readme[readme.index('<!-- Requirements -->'):]
mid_section = "<!-- Last Trends -->\n### Last Trends\n* "+'\n* '.join(trends)+"\n> "+str(datetime.now())+"\n\n"

with open('README.md','w') as file:
    file.write(first_section+mid_section+last_section)
