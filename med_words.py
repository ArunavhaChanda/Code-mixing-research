import eng_search as eng
import beng_search as beng
import re
import editdistance

#fin=open("./BanglaEnglish_FIRE2013_AnnotatedDev.txt",'r')
fin=open("./real_tags.txt",'r')
words=[]
langs=[]
word_cnt = 0
b2e_count=0
e2b_count=0
sent=fin.readline()
while(sent):
	############ Only for Facebook corpus (COMMENT for FIRE)
	#sent = re.sub(r'[^\w\s]','',sent)
	##########################################
	#words=[]
	sent=sent.split()
	for elem in sent:
		word_cnt+=1
		############ Only for FIRE CORPUS (COMMENT for Facebook)
		elem=elem.split('\\')
		#lang = (elem[1][0])
		lang=elem[1]
		word = elem[0]
		#################################
		word=word.strip()
		words.append(word)
		langs.append(lang)
#		if (lang=='B' and eng.eng_search(word)):
#			print(word)
#			b2e_count+=1
#		elif (lang=='E' and beng.beng_word(word)):
#			print(word)
#			e2b_count+=1

	sent=fin.readline()

for i in range(len(words)):
	for j in range(i+1,len(words)):
		if((langs[i]==langs[j] and langs[i]=='B') and (editdistance.eval(words[i].lower(),words[j].lower())==1)):
			print(words[i]+" "+words[j])


#print("Ambiguous words (Beng could be Eng): "+str(b2e_count))
#print("Ambiguous words (Eng could be Beng): "+str(e2b_count))
#print("Total words: "+str(word_cnt))