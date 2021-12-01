import requests as req
from bs4 import BeautifulSoup


def ndtv_scraper(url,path,req_type):

        link = url
        link = req.get(link)
        soup = BeautifulSoup(link.text, 'html.parser')
        result=soup.find_all('div',attrs={'class':'ins_storybody'})

        result = soup.find_all('p')

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
        if req_type==1:
            name = "/Users/mohit/Desktop/project/ranking_pro/ranking_code/og_file/og_article"
        elif req_type==2:
            name=path  
            
        
        file = open(name, "a")

        for x in article:
            file.write(x)
        file.close()





