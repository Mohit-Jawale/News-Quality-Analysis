from textblob import TextBlob
from hindu_scraper import hindu_scraper
from ht_scraper import ht_scraper
from ndtv_scraper import ndtv_scraper
from ie_scraper import ie_scraper
from Emotive import *
import nltk
from score_card import score_card
from hindu_head import *
from ht_head import *
from ndtv_head import *
from ie_head import *


def ranking_filter(s_sites,url):
	s_sites.append(url)
	
	sc_board=[]
	sites=[]

	for site in s_sites:

		score=0
		
		site_name=find_s_name(site)
		
		lines=[]
		if site_name=="www.thehindu.com":
			path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/thehindu/the_hindu_article"
			hindu_scraper(site,path,2)
			article=open(path,'r')
			lines=article.read()
			article.close()

		elif site_name=="www.hindustantimes.com":
			path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ht/the_hindu_article"
			ht_scraper(site,path,2)
			article=open(path,'r')
			lines=article.read()
			article.close()	

		elif site_name=="www.ndtv.com":
			path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ndtv/the_hindu_article"
			ndtv_scraper(site,path,2)
			article=open(path,'r')
			lines=article.read()
			article.close()

		elif site_name=="indianexpress.com":
			path="/Users/mohit/Desktop/project/ranking_pro/ranking_code/similar_articles/ie/the_hindu_article"
			ie_scraper(site,path,2)	
			article=open(path,'r')
			lines=article.read()
			article.close()	

		#sentimental analsis on content
		wiki=TextBlob(lines)
		emotion_num=wiki.sentiment.polarity+wiki.sentiment.subjectivity
		if 0.0<=emotion_num<0.1:
			score=score+10

		elif 0.1<=emotion_num<0.2:
			score=score+9

		elif 0.2<=emotion_num<0.3:
			score=score+8

		elif 0.3<=emotion_num<0.4:
			score=score+7

		elif 0.4<=emotion_num<0.5:
			score=score+6

		elif 0.5<=emotion_num<0.6:
			score=score+5

		elif 0.6<=emotion_num<0.7:
			score=score+4

		elif 0.7<=emotion_num<0.8:
			score=score+3

		elif 0.8<=emotion_num<0.9:
			score=score+2

		else:
			score=score+1

		
		#emotive words analysis
		tokens = nltk.word_tokenize(lines)
		#1.curiosity total 23
		
		count=0
		for x in curiosity:
			if x in tokens:
				count=count+1
		
		y=1+(((count-0)*(10-1))/22)
		

		#2.urgency total 41

		count=0
		for x in urgency:
			if x in tokens:
				count=count+1
		
		y=y+1+(((count-0)*(10-1))/41)
		
		
		#3.helplessness total 55
		count=0
		for x in helplessness:
			if x in tokens:
				count=count+1
		
		y=y+1+(((count-0)*(10-1))/54)
	
		
		#4.Anger total=68
		count=0
		for x in anger:

			if x in tokens:
				count=count+1;
		
		y=y+1+(((count-0)*(10-1))/68)
		
		
		#5.satisfied total=50			
		count=0
		for x in satisfied:
			if x in tokens:
				count=count+1;
		
		y=y+1+(((count-0)*(10-1))/49)
		
		
		#6.happy total=53
		count=0
		for x in happy:
			if x in tokens:
				count=count+1;
		
		y=y+1+(((count-0)*(10-1))/52)
		
		
		#7.peaceful total=50
		count=0
		for x in peaceful:
			if x in tokens:
				count=count+1;
		
		y=y+1+(((count-0)*(10-1))/49)
		
		
		#8.inspired total=43
		count=0
		for x in inspired:
			if x in tokens:
				count=count+1;
		y=y+1+(((count-0)*(10-1))/22)
	
		y=y/8 #taking average of it

		score=score+y
		#part of speech analysis
		
		pro_count=0
		verb_count=0
		adj_count=0
		adverb_count=0
		for index in range(0,len(wiki.tags)-1):
			if wiki.tags[index][1] in ['NNP','NPPS','PRP','PRP$','WP$']:
				pro_count=pro_count+1
			elif wiki.tags[index][1] in ['JJ','JJR','JJS']:
				adj_count=adj_count+1
			elif wiki.tags[index][1] in ['RB','RBR','RBS','WRB']:
				adverb_count=adverb_count+1	
			elif wiki.tags[index][1] in ['VB','VBD','VBG','VBN','VBP','VBZ']:
				verb_count=verb_count+1

		
		

		diff_adj=pro_count-adj_count
		diff_adverb=pro_count-adverb_count	
		diff_verb=pro_count-verb_count

		diff_per_adj=(diff_adj/(pro_count+adj_count))*100
		diff_per_adverb=(diff_adverb/(pro_count+adverb_count))*100	
		diff_per_verb=(diff_verb/(pro_count+verb_count))*100

		adj_score=score_card(diff_per_adj)
		adverb_score=score_card(diff_per_adverb)
		verb_score=score_card(diff_per_verb)

		score=adj_score+adverb_score+verb_score

		#headline analysis
		headline=""
		if site_name=="www.thehindu.com":
			headline=hindu_head(site)	
		elif site_name=="www.hindustantimes.com":
			headline=ht_head(site)
		elif site_name=="www.ndtv.com": 
			headline=ndtv_head(site)
		elif site_name=="indianexpress.com":
			headline=ie_head(site)	

		head_score=0
		head_wiki=TextBlob(headline)
	
		
		for index in range(0,len(head_wiki.tags)-1):
			if head_wiki.tags[index][1] == "CD":
				head_score=head_score+1

		
		for index in range(0,len(head_wiki.tags)-1):
			if head_wiki.tags[index][1] in ['VB','VBD','VBG','VBN','VBP','VBZ']:
				head_score=head_score+1

				
		for index in range(0,len(head_wiki.tags)-1):
			if head_wiki.tags[index][1] == "JJS":
				head_score=head_score+1

		if '-' in headline:
			head_score=head_score+1				
			

		if head_score==4:
			score=score+10	
		elif headline==3:
			score=score+7.5
		elif headline==2:
			score=score+5
		elif headline==1:
			score=score+2.5
		sc_board.append(score)
		sites.append(site)	
			
		
						

	return list(zip(sc_board,sites))	







		



def find_s_name(url):
	#print(url)
	x=url.split("/")
	x.pop(0)
	x.pop(0)
	return x[0]