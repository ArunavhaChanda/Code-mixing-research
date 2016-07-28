# coding=utf-8
from unidecode import unidecode
import re
import editdistance
import fileinput
from nltk.corpus import brown

val=editdistance.eval('byaapk','byapak')
print (val)

word = unidecode("চোখা")
print (word)

line = "No No No [ Yes ] No No No"

lst=[1,2,3,4,5,6,7,8]
for num in lst:
	if(num==3):
		print(str(num)+" is at index "+str(lst.index(num)))


lst=line.split("[")
lst=lst[1].split("]")
lst=lst[0].strip(" ")
lst=lst.split(",")
for i in range(len(lst)):
	lst[i]=lst[i].strip(" ")
	print (lst[i])

'''
if(lst=="Yes"):
	print ("Yippeee")

katha="mother"
kat=katha[0:-1]
print (kat)
'''

'''
files=["abd.txt","amitava.txt","bd.txt","chan.txt","chandan.txt","deb.txt","jit.txt","jyotirmoy.txt","kunal.txt","mainak.txt","manika.txt","moy.txt","msm.txt","padma.txt","plb.txt","punam.txt","rajashree.txt","rita.txt","samaresh.txt","sandi.txt","sayan.txt","swarnendu.txt"]
comp=open("./beng_train.txt",'w')
for file in files:
	samp=open(file)
	line=samp.readline()
	while(line):
		line = re.sub(r'[^\w\s]','',line)
		line=line.split()
		for word in line:
			word=word.strip()
			if(len(word)>=2):
				if(word[-1]=='a'):
					word=word[0:-1]
			word=word.lower()
			comp.write(word+" ")
		line=samp.readline()
	samp.close()
comp.close()


'''
comp=open("./beng_train.txt",'r')
line=comp.readline()
line=line.split()
print("Words in Bengali corpus: "+str(len(line)))
comp.close()


norm1 = open("eng_normalize_dict.txt",'r')
norm2 = open("norm_2.txt",'r')
wrong_words = open("bad_eng.csv",'w')

line=norm1.readline()
while(line):
	line=line.split()
	line=line[0].strip(" ")
	wrong_words.write(line+", ")
	line = norm1.readline()
norm1.close()

line=norm2.readline()
while(line):
	line=line.split('|')
	line=line[0].split()
	line=line[1].strip(" ")
	wrong_words.write(line+", ")
	line = norm2.readline()
norm2.close()
wrong_words.close()

'''
dic=open("./beng_dict.txt",'r')
word_list=open("./beng_words.txt",'w')
line = dic.readline()
line=unidecode(line)
while (line):
	copy=line
	if copy.strip():
		lst=line.split("[")
		key=lst[0].strip(" ")
		lst=lst[1].split("]")
		phone=lst[0].strip(" ")
		key=key.split(",")
		phone=phone.split(",")
		for i in range(len(key)):
			key[i]=key[i].strip(" ")
			phone[i]=phone[i].strip(" ")
			key[i]=key[i].lower()
			phone[i]=phone[i].lower()
			if(len(key[i])>=2):
				if(key[i][-1].isdigit()):
					key[i]=key[i][0:-1]
			if(len(phone[i])>=2):
				if(phone[i][-1].isdigit()):
					phone[i]=phone[i][0:-1]
				if(phone[i][-1]=='a'):
					edit_phone=phone[i][0:-1]
					if(len(edit_phone)>=1):
						word_list.write(edit_phone+", ")
			if(len(key[i])>=1):
				word_list.write(key[i]+", ")
			if(len(phone[i])>=1):
				word_list.write(phone[i]+", ")
	line = dic.readline()
	line=unidecode(line)
dic.close()
word_list.close()
'''

'''
text=" ".join(brown.words())

text=text.split()
print("Words in English corpus: "+str(len(text)))


for i in range(1,11):
	if i!=5:
		print (i)
#for line in fileinput.FileInput("./eng_stop.txt",inplace=1):
 #      print (line)
'''


'''
fin=open("./beng_corpus.txt",'r')
fout=open("./beng_ac_corpus.txt",'w')
line=fin.readline()
while(line):
	line=line.split()
	for word in line:
		word=word.strip()
		fout.write(word+'\B ')
	fout.write('\n')
	line=fin.readline()
fin.close()
fout.close()
'''

'''
fin=open("./beng_corpus.txt",'r')
count=0
line=fin.readline()
while(line):
	line=line.split()
	for word in line:
		count+=1
	line=fin.readline()
fin.close()
print("Total words: "+str(count))
'''


'''
fin = open("./Bengali_Verb_Inflection.txt",'r')
fout=open("./beng_affix.txt",'w')
line = fin.readline().decode('utf-8')
while (line):
	if(line.strip()):
		line=line.strip()
		line=unidecode(line)
		fout.write(line)
	line=fin.readline().decode('utf-8')
fin.close()
fout.close()

'''
'''

words=['first','second']
print(words[1][0])
'''