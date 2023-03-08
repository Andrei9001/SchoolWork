from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

class News:
    def __init__(self,url,elmt,clas,print):
        self.url = url
        self.elmt = elmt
        self.clas = clas
        self.print = print

    def scrape(self):
        response = requests.get(self.url)
        htts = response.text
        soup = BeautifulSoup(htts, 'html.parser')
        return soup

    def headline(self):
        headline = self.scrape().head.title.text
        return headline

    def article(self):
        global articles
        
        headlines = self.scrape().find('body').find_all(self.elmt,class_=self.clas)
        for x in headlines:
            temp =[]
            head = x.text.strip()
            if self.print is True:
                print(head)
            temp.append(head)
            if temp ==['']: continue
            
            if head not in articles: 
                articles.append(temp)
                temp =[]
            else: continue
            

news =[["https://www.tvnet.lv",'div','list-article__headline'],['https://www.delfi.lv/','span','headline__title'],['https://www.lsm.lv/','span','thumbnail__caption_text'],['https://www.ntz.lv/','h3','article-title'],['https://www.apollo.lv/','div','list-article__headline']]
articles = []
choice = int(input('Izvēleties ziņu lapu:\n1.TVnet\n2.Delfi\n3.LSM\n4.Neatkarīgās Tukuma ziņas\n5.Apollo\nIevadiet skaitli šeit: '))
html1 = News(news[0][0],news[0][1],news[0][2],True)
html2 = News(news[1][0],news[1][1],news[1][2],True)
html3 = News(news[2][0],news[2][1],news[2][2],True)
html4 = News(news[3][0],news[3][1],news[3][2],True)
html5 = News(news[4][0],news[4][1],news[4][2],True)

if choice == 1: html = html1
elif choice == 2:html = html2
elif choice == 3:html = html3
elif choice == 4:html = html4
elif choice == 5:html = html5

html.article()


#   Izveido CSV ar visiem rakstiem palaišanas dienā
time = datetime.now()
day = time.strftime("%d-%m-%Y")
path  ='All_news_{}.csv'.format(day)

for i in news:
    total = News(i[0],i[1],i[2],False)
    total.article()

    with open(path,'w',encoding='utf-8',newline='') as t:
        csw_writer = csv.writer(t)
        csw_writer.writerow(['Article'])
        csw_writer.writerows(articles)

