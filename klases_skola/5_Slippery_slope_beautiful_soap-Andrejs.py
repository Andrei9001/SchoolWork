from bs4 import BeautifulSoup
import requests
import csv

class News:
    def __init__(self,url,elmt,clas):
        self.url = url
        self.elmt = elmt
        self.clas = clas
        
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
            head = x.text.strip()
            print(head)
            if head not in articles: articles.append(head)
            else: continue
            

news =[["https://www.tvnet.lv",'div','list-article__headline'],['https://www.delfi.lv/','span','headline__title'],['https://www.lsm.lv/','span','thumbnail__caption_text'],['https://www.ntz.lv/','h3','article-title'],['https://www.apollo.lv/','div','list-article__headline']]
articles = []
choice = int(input('Izvēleties ziņu lapu:\n1.TVnet\n2.Delfi\n3.LSM\n4.Neatkarīgās Tukuma ziņas\n5.Apollo\nIevadiet skaitli šeit: '))
html1 = News(news[0][0],news[0][1],news[0][2])
html2 = News(news[1][0],news[1][1],news[1][2])
html3 = News(news[2][0],news[2][1],news[2][2])
html4 = News(news[3][0],news[3][1],news[3][2])
html5 = News(news[4][0],news[4][1],news[4][2])

if choice == 1: html = html1
elif choice == 2:html = html2
elif choice == 3:html = html3
elif choice == 4:html = html4
elif choice == 5:html = html5

print(html.article())
for i in news:
    

