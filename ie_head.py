import requests as req
from bs4 import BeautifulSoup

def ie_head(url):
        link = url
        link = req.get(link)
        soup = BeautifulSoup(link.text, 'html.parser')
        result=soup.find_all('h1',attrs={'class':"m-story-header__title"})

        article = []
        l1 = len(result)
        flag=0
        i = 0
        while i < l1:
            j = 0
            exp = result[i]  # this is pne array of paragraph
            l = len(exp)
            while j < l:
                
                article.append(exp.contents[j].string)
                j = j+1
            if flag == 1:
                flag = 0
                break
            i = i+1

        # article.pop(0)
        article = [x for x in article if x is not None]
        return article[0]