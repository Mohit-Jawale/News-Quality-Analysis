import requests as req
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from similar_context import context_similarity
from ranking_logic import ranking_filter
import nltk 






def ranking(url):
    site_name=find_site_name(url)
    highlight_words=parse_link(site_name,url)
    s_sites=find_similar_sites(site_name,highlight_words,url)
    score_inc=ranking_filter(s_sites,url)
    score_inc.sort(reverse=True)
    return score_inc
 
    
   


 
    








def find_similar_sites(site_name,highlight_words,og_url):
     
    num_sites={

    1:"www.thehindu.com",

    2:"www.hindustantimes.com",

    3:"www.ndtv.com",

    4:"indianexpress.com",

    5:"zeenews.india.com"
     

    }

     
    similar_sites_list=[]
    similar_sites=[]
   
    #here multiprocessing can be used
    for index in range(1,5):
     	if site_name!=num_sites[index]:
     	 	similar_sites.append(sitemap_scarping(index,highlight_words,og_url))


  
    return similar_sites
     	 	
    
         
  



def sitemap_scarping(index,highlight_words,og_url):

	if index==1:
		
		url = req.get("https://www.thehindu.com/sitemap/googlenews/all/1.xml")
		soup = BeautifulSoup(url.text, 'xml')
		sitemap = []
		for i in soup.find_all('loc'):
			sitemap.append(i.text)
		max_word=0
		similar_url=""
		max_list=[]
		stop_words = stopwords.words('english')
		highlight_words=[word for word in highlight_words if word not in stop_words]
			

		for x in sitemap:
			URL=x
			list1d=hindu_parser(URL)
			list1d=[word for word in list1d if word not in stop_words]
			count=0
			sim_count=0
	
	#algo   
			for word in highlight_words:
				if word in list1d:
					count=count+1

			if max_word<count:
				max_word=count
				similar_url=URL
			elif max_word==count and count!=0:
				similar_url=context_similarity(URL,similar_url,og_url)
				similar_words=hindu_parser(similar_url)
				for word in highlight_words:
					if word in similar_words:
						sim_count=sim_count+1
				max_word=sim_count
				
				
		#print(highlight_words)
		#print(max_word)		
		return similar_url

	if index==2:
		
		url = req.get("https://www.hindustantimes.com/sitemap/today")
		soup = BeautifulSoup(url.text, 'xml')
		sitemap = []
		for i in soup.find_all('loc'):

			sitemap.append(i.text)

		max_word=0
		similar_url=""
		max_list=[]
		stop_words = stopwords.words('english')
		highlight_words=[word for word in highlight_words if word not in stop_words]		

		for x in sitemap:
			URL=x
			list1d=hindu_parser(URL)
			count=0
			sim_count=0

	
	#algo
			for word in highlight_words:
				if word in list1d:
					count=count+1

			if max_word<count:
				max_word=count
				similar_url=URL	
			elif max_word==count and count!=0:
				similar_url=context_similarity(URL,similar_url,og_url)
				similar_words=hindu_parser(similar_url)
				for word in highlight_words:
					if word in similar_words:
						sim_count=sim_count+1
				max_word=sim_count	
		#print(max_word)	    	
		return similar_url
       
	if index==3:
		
		url = req.get("https://www.ndtv.com/sitemap.xml")
		soup = BeautifulSoup(url.text, 'xml')
		psuedo_sitemap = []
		for i in soup.find_all('loc'):

			psuedo_sitemap.append(i.text)
		data=psuedo_sitemap[0]
		data=req.get(data)
		soup=BeautifulSoup(data.text,'xml')
		#print(soup)
		sitemap=[]
		for url in soup.find_all('loc'):
			sitemap.append(url.text)
        
			
		max_word=0
		similar_url=""
		max_list=[]
		stop_words = stopwords.words('english')
		highlight_words=[word for word in highlight_words if word not in stop_words]		

		for x in sitemap:
			URL=x
			list1d=ndtv_parser(URL)
			count=0
			sim_count=0
	
	#algo
			for word in highlight_words:
				if word in list1d:
					count=count+1

			if max_word<count:
				max_word=count
				similar_url=URL
			elif max_word==count!=0:
				similar_url=context_similarity(URL,similar_url,og_url)
				similar_words=ndtv_parser(similar_url)
				for word in highlight_words:
					if word in similar_words:
						sim_count=sim_count+1
				max_word=sim_count
		#print(max_word)			
		return similar_url

	if index==4:
		
		url = req.get("https://indianexpress.com/news-sitemap.xml")
		soup = BeautifulSoup(url.text, 'xml')
		sitemap = []
		for i in soup.find_all('loc'):
			sitemap.append(i.text)
		max_word=0
		similar_url=""
		max_list=[]
		stop_words = stopwords.words('english')
		highlight_words=[word for word in highlight_words if word not in stop_words]
			

		for x in sitemap:
			URL=x
			list1d=ndtv_parser(URL)
			list1d=[word for word in list1d if word not in stop_words]
			count=0
			sim_count=0
	
	#algo   
			for word in highlight_words:
				if word in list1d:
					count=count+1

			if max_word<count:
				max_word=count
				similar_url=URL
			elif max_word==count and count!=0:
				similar_url=context_similarity(URL,similar_url,og_url)
				similar_words=hindu_parser(similar_url)
				for word in highlight_words:
					if word in similar_words:
						sim_count=sim_count+1
				max_word=sim_count
				
				
		#print(highlight_words)
		#print(max_word)		
		return similar_url	
           


    







def hindu_parser(url):
	x=url.split("/")
	x.pop(0)
	x.pop(0)
	x.pop(0)
	x.pop()
	tokens=[]

	for txt in x:
		tokens.append(txt.split("-"))

#reducing it into 1d array
	highlight_words=[]
	highlight_words=[j for sub in tokens for j in sub]
	return highlight_words

def ndtv_parser(url):
	x=url.split("/")
	x.pop(0)
	x.pop(0)
	x.pop(0)
	tokens=[]
	for txt in x:
		tokens.append(txt.split("-"))

	highlight_words=[]
	highlight_words=[j for sub in tokens for j in sub]
	highlight_words.pop()
	return highlight_words


def parse_link(sitename,url):
   
    diff_parser={
     
     "www.thehindu.com" : hindu_parser(url),

     "www.hindustantimes.com" : hindu_parser(url),

     "www.ndtv.com" :  ndtv_parser(url),

     "indianexpress.com" : ndtv_parser(url),

     "zeenews.india.com" : ndtv_parser(url)

    }

    return diff_parser[sitename]







def find_site_name(url):
	x=url.split("/")
	x.pop(0)
	x.pop(0)
	return x[0]
