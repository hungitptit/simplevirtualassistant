from GoogleNews import GoogleNews
from datetime import date, datetime
googlenews = GoogleNews()
today = date.today()
date = today.strftime("%d/%m/%Y")
googlenews = GoogleNews(lang='en')
googlenews = GoogleNews(period = 'd')
googlenews.search(' ')
news = googlenews.gettext()
links = googlenews.get__links()
#googlenews.getpage(1)
#result = googlenews.result()
for n in range(len(news)):
    print(news[n])
    #print(links[n])
'''
for n in range(len(result)):
    print(n)
    for index in result[n]:
        print(index, '\n', result[n][index])

 '''