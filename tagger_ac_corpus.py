#import finder_beng as finder
import finder
from collections import defaultdict
import beng_search as beng
import re
from nltk.util import ngrams

def main():
	lno=1
	word_tot=0
	corr=0
	init_corr=0
	fin=open("./beng_corpus.txt",'r')
	fout_pred=open("./predicted_tags_eng.txt",'w')
	fout_corr=open("./corrected_tags_eng.txt",'w')
	sent=fin.readline()
	while(sent):
		sent = re.sub(r'[^\w\s]','',sent)
		words=[]
		sent=sent.split()
		for elem in sent:
			elem.strip()
			words.append(elem)
		type_map = defaultdict(str)
		type_count = defaultdict(int)
		word_count=0
		for word in words:
			word=word.strip(" ")
			word_count+=1
			type_word=finder.find(word)
			type_map[word]=type_word
			type_count[type_word]+=1
			#print(str(word)+"(Detect:"+str(type_map[word])+")")
			if(type_word=="English word"):
				fout_pred.write(word+"\\"+"E ")
			elif(type_word=="Bengali word"):
				fout_pred.write(word+"\\"+"B ")
			else:
				fout_pred.write(word+"\\"+"N ")


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
			if(default=="e"):
				if(beng.beng_word(words[i])==1 and type_map[words[i]]=="English word"):
					if(i>1 and i<(len(words)-2)):
						word_count=4
						for j in range(i-2,min((len(words)-1),(i+3))):
							if(j!=i):
								type_count[type_map[words[j]]]+=1
						if(type_count["Bengali word"]>type_count["English word"]):
							type_map[words[i]]="Bengali word"
					elif (i<=1):
						word_count=min(i+2,len(words)-1)
						for j in range(min((len(words)-1),(i+3))):
							if(j!=i):
								type_count[type_map[words[j]]]+=1
						if(type_count["Bengali word"]>type_count["English word"]):
							type_map[words[i]]="Bengali word"
					elif(i>=(len(words)-2)):
						word_count= (len(words)-i)+1
						for j in range(i-2,len(words)):
							if(j!=i):
								type_count[type_map[words[j]]]+=1
						if(type_count["Bengali word"]>type_count["English word"]):
							type_map[words[i]]="Bengali word"
			elif(default=="b"):
				if(beng.beng_word(words[i])==1 and type_map[words[i]]=="English word"):
					if(i>1 and i<(len(words)-2)):
						word_count=4
						for j in range(i-2,min((len(words)-1),(i+3))):
							if(j!=i):
								type_count[type_map[words[j]]]+=1
						if(type_count["Bengali word"]>=type_count["English word"]):
							type_map[words[i]]="Bengali word"
					elif (i<=1):
						word_count=min(i+2,len(words)-1)
						for j in range(min((len(words)-1),(i+3))):
							if(j!=i):
								type_count[type_map[words[j]]]+=1
						if(type_count["Bengali word"]>=type_count["English word"]):
							type_map[words[i]]="Bengali word"
					elif(i>=(len(words)-2)):
						word_count= (len(words)-i)+1
						for j in range(i-2,len(words)):
							if(j!=i):
								type_count[type_map[words[j]]]+=1
						if(type_count["Bengali word"]>=type_count["English word"]):
							type_map[words[i]]="Bengali word"
			
			if(type_map[words[i]]=="Bengali word"):
				fout_corr.write(words[i]+"\\"+"B ")
			elif(type_map[words[i]]=="English word"):
				fout_corr.write(words[i]+"\\"+"E ")
			else:
				fout_corr.write(words[i]+"\\"+"N ")
		#for word in words:
		#	print (word+": "+type_map[word])
		sent=fin.readline()
	fin.close()
	fout_pred.close()
	fout_corr.close()

main()