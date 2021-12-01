import requests as req
from bs4 import BeautifulSoup

def ht_head(url):
        x=url.split("/")
        x.pop(0)
        x.pop(0)
        x.pop(0)
        x.pop()
        tokens=[]
        for txt in x:
            tokens.append(txt.split("-"))
        high_words=[]
        high_words=[j for sub in tokens for j in sub]    
            
        if ("live" and "updates") in high_words:
         
            return " "
        else:
            
            link = url
            link = req.get(link)
            soup = BeautifulSoup(link.text, 'html.parser')
            result=soup.find_all('div',attrs={'class':"story-highlight"})

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
            

            return article[1]


           