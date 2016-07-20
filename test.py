# coding=utf-8
from unidecode import unidecode
import re
import editdistance
import fileinput

val=editdistance.eval('byaapk','byapak')
print (val)

word = unidecode("বৃষ্টি [ bṛṣṭi ]")
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

for i in range(1,11):
	if i!=5:
		print (i)
#for line in fileinput.FileInput("./eng_stop.txt",inplace=1):
 #      print (line)
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