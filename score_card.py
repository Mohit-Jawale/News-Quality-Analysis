def score_card(score):
	a_score=0
	if 0<=score<10:
		a_score=a_score+1
	elif 10<=score<20:
		a_score=a_score+2	
	elif 20<=score<30:
		a_score=a_score+3	
	elif 30<=score<40:
		a_score=a_score+4	
	elif 40<=score<50:
		a_score=a_score+5							
	elif 50<=score<60:
		a_score=a_score+6			
	elif 60<=score<70:
		a_score=a_score+7	
	elif 70<=score<80:
		a_score=a_score+8					
	elif 80<=score<90:
		a_score=a_score+9	
	elif 90<=score<=100:
		a_score=a_score+10					

	return a_score	