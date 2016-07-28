# coding=utf-8
from unidecode import unidecode
import editdistance

def beng_word(word):
	word=word.lower()
	bengdict = open("./beng_words.txt",'r')
	line = bengdict.readline()
	line = line.split(",")
	for dict_word in line:
		dict_word=dict_word.strip()
		'''
		if(editdistance.eval(phone[i].lower(),word.lower())<=1 or editdistance.eval(key[i].lower(),word.lower())<=1):
			print("1"+key[i]+" "+phone[i])
			bengdict.close()
			return 1
		'''
		if(editdistance.eval(dict_word.lower(),word.lower())<=1):
			bengdict.close()
			return 1

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