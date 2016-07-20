import finder_beng as finder
from collections import defaultdict
import beng_search as beng

def main():
	lno=1
	word_tot=0
	corr=0
	fin=open("./BanglaEnglish_FIRE2013_AnnotatedDev.txt",'r')
	sent=fin.readline()
	while(sent):
		words=[]
		lang=[]
		sent=sent.split()
		for elem in sent:
			elem=elem.split('\\')
			lang.append(elem[1][0])
			words.append(elem[0])
		type_map = defaultdict(str)
		type_count = defaultdict(int)
		word_count=0
		for word in words:
			word=word.strip(" ")
			word_count+=1
			type_word=finder.find(word)
			type_map[word]=type_word
			type_count[type_word]+=1
		'''
		for word in words:
			print (word+": "+type_map[word])
		print("Type count of English: "+str(type_count["English word"]))
		print("Type count of Bengali: "+str(type_count["Bengali word"]))
		'''
		if((type_count["English word"])>(type_count["Bengali word"])):
			default="e"
		else:
			default="b"
		print(str(lno)+default)
		lno+=1
		for i in range(len(words)):
			word_count=0
			type_count["English word"]=0
			type_count["Bengali word"]=0
			if((type_map[words[i]]=="Bengali word" and lang[i]=='B') or (type_map[words[i]]=="English word" and lang[i]=='E')):
				corr+=1
			word_tot+=1
		#for word in words:
		#	print (word+": "+type_map[word])
		sent=fin.readline()
	print("The accuracy is: "+str(corr*100/word_tot)+"%")

main()