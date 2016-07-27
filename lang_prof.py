from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
import sys
import operator

ngrams_statistics={}

def main(argv):
	filename=argv[0]
	fin=open(filename,'r')
	line=fin.readline()
	count=0
	while(line):
		tokenizer = RegexpTokenizer("[a-zA-Z'`]+")
		words = tokenizer.tokenize(line)
		for word in words:
			count+=1
			print(str(count)+word)
			grams = ngrams(word,4,pad_left=True,pad_right=True,left_pad_symbol=' ',right_pad_symbol=' ')
			grams=list(grams)
			ng_list=[]
			for j in range (len(grams)):
				ng_list.append(''.join(grams[j]))
			ngram_hash(ng_list)
		line=fin.readline()
	ngrams_statistics_sorted = sorted(ngrams_statistics.items(), key=operator.itemgetter(1), reverse=True) [0:400]
	print(str(ngrams_statistics_sorted[80:90]))
	fin.close()

def ngram_hash(ng_list):
	for ngram in ng_list:
		if ngram not in ngrams_statistics:
			ngrams_statistics.update({ngram:1})
		else:
			ngram_occurrences = ngrams_statistics[ngram]
			ngrams_statistics.update({ngram:ngram_occurrences+1})

main(sys.argv[1:])