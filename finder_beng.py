import search as eng
import beng_search as beng

def find(word):
	if (beng.beng_word(word)):
		return ("Bengali word")
	elif (eng.eng_word(word)):
		return ("English word")
	else:
		return ("Not a word")