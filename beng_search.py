# coding=utf-8
from unidecode import unidecode
import editdistance

def beng_word(word):
	bengdict = open("./beng_dict.txt",'r')
	line = bengdict.readline()
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
				if(editdistance.eval(phone[i].lower(),word.lower())<=1 or editdistance.eval(key[i].lower(),word.lower())<=1):
#					print(key[i])
					bengdict.close()
					return 1
				if(len(phone[i])>=1 and len(key[i])>=1):
					if (phone[i][-1]=='a' or key[i][-1]=='a'):
						if(editdistance.eval((phone[i][0:-1]).lower(),word.lower())<=1 or editdistance.eval((key[i][0:-1]).lower(),word.lower())<=1):
#							print(key[i])
							bengdict.close()
							return 1
		line = bengdict.readline()
		line=unidecode(line)
	bengdict.close()
	beng_suff = open("./beng_suffix.csv",'r')
	suff_list = beng_suff.readline().split(",")
	for suff in suff_list:
		suff=suff.strip(" ")
		if ((word.find(suff,2)==(len(word)-len(suff))) and len(word)>len(suff)):
			beng_suff.close()
			return 1
	beng_suff.close()
	return 0