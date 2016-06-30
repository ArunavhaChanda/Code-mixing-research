import search as eng
import beng_search as beng

def find(word):
	if (eng.eng_word(word)):
		return ("English word")
	elif (beng.beng_word(word)):
		return ("Bengali word")
	else:
		return ("Not a word")