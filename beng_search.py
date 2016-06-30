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
					bengdict.close()
					return 1
				elif(editdistance.eval((phone[i][0:-1]).lower(),word.lower())<=1 or editdistance.eval((key[i][0:-1]).lower(),word.lower())<=1):
					bengdict.close()
					return 1
		line = bengdict.readline()
		line=unidecode(line)
	bengdict.close()
	return 0