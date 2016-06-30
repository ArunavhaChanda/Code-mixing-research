import finder
from collections import defaultdict
import beng_search as beng

def main():
	type_map = defaultdict(str)
	type_count = defaultdict(int)
	word_count=0
	sentence=input("Please enter your sentence: ")
	words=sentence.split()
	for word in words:
		word=word.strip(" ")
		word_count+=1
		type_word=finder.find(word)
		type_map[word]=type_word
		type_count[type_word]+=1
	for word in words:
		print (word+": "+type_map[word])
	print("Type count of English: "+str(type_count["English word"]))
	print("Type count of Bengali: "+str(type_count["Bengali word"]))
	if((type_count["English word"])>(type_count["Bengali word"])):
		default="e"
	else:
		default="b"
	print(default)
	for i in range(len(words)):
		word_count=0
		type_count["English word"]=0
		type_count["Bengali word"]=0
		if(default=="e"):
			if(beng.beng_word(words[i])==1 and type_map[words[i]]=="English word"):
				if(i>1 and i<(len(words)-2)):
					word_count=4
					for j in range(i-2,i+3):
						if(j!=i):
							type_count[type_map[words[j]]]+=1
					if(type_count["Bengali word"]>type_count["English word"]):
						type_map[words[i]]="Bengali word"
				elif (i<=1):
					word_count=i+2
					for j in range(i+3):
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
					for j in range(i-2,i+3):
						if(j!=i):
							type_count[type_map[words[j]]]+=1
					if(type_count["Bengali word"]>=type_count["English word"]):
						type_map[words[i]]="Bengali word"
				elif (i<=1):
					word_count=i+2
					for j in range(i+3):
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

	for word in words:
		print (word+": "+type_map[word])

main()