import enchant

def eng_search(word):
	word=word.lower()
	d=enchant.Dict("en_US")
	if (d.check(word)):
		return 1
	bad=open("./bad_eng.csv",'r')
	bad_words=bad.readline().split(",")
	for bad_word in bad_words:
		bad_word=bad_word.strip(" ")
		if(word==bad_word.lower()):
			return 1
	return 0