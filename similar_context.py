import os.path
from os import path
from hindu_scraper import hindu_scraper
from ht_scraper import ht_scraper
from ndtv_scraper import ndtv_scraper
from ie_scraper import ie_scraper
import nltk
from nltk.corpus import stopwords







def context_similarity(url,similar_url,og_url)	:

	#OG_url scraper
	
	og_site_name=find_s_name(og_url)
	og_path= "/Users/mohit/Desktop/project/ranking_pro/ranking_code/og_file/og_article"
	

	if og_site_name=="www.thehindu.com":
		if path.exists("og_file/og_article")==False:
			hindu_scraper(og_url,og_path,1)
    
	elif og_site_name=="www.hindustantimes.com":
		if path.exists("og_file/og_article")==False:
			ht_scraper(og_url,og_path,1)

	elif og_site_name=="www.ndtv.com":
			if path.exists("og_file/og_article")==False:
				ndtv_scraper(og_url,og_path,1)

	elif og_site_name=="indianexpress.com":
			if path.exists("og_file/og_article")==False:
				ie_scraper(og_url,og_path,1)
    

    

  #similar url scraping

	similar_site_name=find_s_name(similar_url)
	

	if similar_site_name=="www.thehindu.com":
		s_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/thehindu/article"
		hindu_scraper(similar_url,s_path,2)
    
	elif similar_site_name=="www.hindustantimes.com":
		s_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ht/article"
		ht_scraper(similar_url,s_path,2)

	elif similar_site_name=="www.ndtv.com":
		s_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ndtv/article"
		ndtv_scraper(similar_url,s_path,2)
		
				
	elif similar_site_name=="indianexpress.com":
		s_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ie/article"
		ie_scraper(similar_url,s_path,2)

		
   
#new_url
	newurl_site_name=find_s_name(url)
	

	if  newurl_site_name=="www.thehindu.com":
		n_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/thehindu/article"
		hindu_scraper(url,n_path,2)
    
	elif newurl_site_name=="www.hindustantimes.com":
		n_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ht/article"
		ht_scraper(url,n_path,2)

	elif newurl_site_name=="www.ndtv.com":
		n_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ndtv/article"
		ndtv_scraper(url,n_path,2)
		
				
	elif newurl_site_name=="indianexpress.com":
		n_path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ie/article"
		ie_scraper(url,n_path,2)

	decide=comparison_of_similarity(similar_site_name,newurl_site_name)	
	if decide==1:
		return url
	else:
		return similar_url	





def comparison_of_similarity(s_sitename,new_sitename):

#open og file
	og_path = "/Users/mohit/Desktop/project/ranking_pro/ranking_code/og_file/og_article"
	file=open(og_path,'r')
	lines=[]
	lines=file.read()
	tokens = nltk.word_tokenize(lines)
	lower_tokens=[]
	for i in tokens:
		lower_tokens.append(i.lower())
	stop_words = stopwords.words('english')
	og_words=[word for word in lower_tokens if word not in stop_words]
	file.close()
	#print(og_words)
#open similar word file

	s_path={

     "www.thehindu.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/thehindu/article",

     "www.hindustantimes.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ht/article",

     "www.ndtv.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ndtv/article",

     "indianexpress.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ie/article",

     "zeenews.india.com" : "/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ie/article"
  

	}
	sim_path = s_path[s_sitename]
	file=open(sim_path,'r')
	lines=[]
	lines=file.read()
	sim_tokens = nltk.word_tokenize(lines)
	sim_low_tokens=[]
	for i in sim_tokens:
		sim_low_tokens.append(i.lower())
	stop_words = stopwords.words('english')
	sim_words=[word for word in sim_low_tokens if word not in stop_words]
	file.close()
#new_url code
	new_path={

     "www.thehindu.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/thehindu/article",

     "www.hindustantimes.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ht/article",

     "www.ndtv.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ndtv/article",

     "indianexpress.com" :"/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ie/article",

     "zeenews.india.com" : "/Users/mohit/Desktop/project/ranking_pro/ranking_code/new_articles/ie/article"
  

	}

	n_path = new_path[new_sitename]
	file=open(n_path,'r')
	lines=[]
	lines=file.read()
	n_tokens = nltk.word_tokenize(lines)
	n_low_tokens=[]
	for i in n_tokens:
		n_low_tokens.append(i.lower())
	stop_words = stopwords.words('english')
	new_words=[word for word in n_low_tokens if word not in stop_words]
	file.close()
	os.remove(str(n_path))
	os.remove(str(sim_path))

	#similarity algo


	sim_comp=[]
	sim_countt=0
	new_count=0
	new_comp=[]
	for x in og_words:
		if x in sim_words:
			sim_comp.append(x)
			sim_comp.append(1)
			sim_countt=sim_countt+1


	for x in og_words:
		if x in new_words:
			new_comp.append(x)
			new_comp.append(1)
			new_count=new_count+1
	#print(sim_count)
	#print(new_count)		
	if new_count>=sim_countt:
		return 1
		
		
def find_s_name(url):
	#print(url)
	x=url.split("/")
	x.pop(0)
	x.pop(0)
	return x[0]












