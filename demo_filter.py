from ranking_logic import ranking_filter
from ndtv_head import *
from hindu_head import *
from ie_head import *
from ht_head import *

sites=['https://www.ndtv.com/india-news/naveen-patnaik-takes-oath-as-odisha-chief-minister-for-fifth-term-2044622', 'https://indianexpress.com/elections/naveen-patnaik-takes-oath-as-odisha-chief-minister-for-fifth-term-5753883/', 'https://www.thehindu.com/elections/odisha-assembly/naveen-patnaik-takes-oath-as-odisha-chief-minister-20-ministers-also-sworn-in/article27282466.ece?homepage=true','https://www.hindustantimes.com/india-news/live-updates-naveen-patnaik-takes-oath-as-odisha-cm-for-his-fifth-consecutive-term/story-SfdTjwX4tv7mncPB3Pg3VM.html']
#print(len(sites))
ranking_filter(sites)

#ndtv_head("https://www.ndtv.com/india-news/naveen-patnaik-takes-oath-as-odisha-chief-minister-for-fifth-term-2044622")
#hindu_head("https://www.thehindu.com/elections/odisha-assembly/naveen-patnaik-takes-oath-as-odisha-chief-minister-20-ministers-also-sworn-in/article27282466.ece?homepage=true")
#ie_head("https://indianexpress.com/elections/naveen-patnaik-takes-oath-as-odisha-chief-minister-for-fifth-term-5753883/")
##ht_head("https://www.hindustantimes.com/world-news/in-nirav-modi-extradition-case-india-s-paperwork-under-focus-in-london-court/story-2JtfwYJGra7LrZ9Y1GtGcP.html")