from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
import sys
import operator

def ngram_prof(filename,ngrams_statistics):
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
			ngrams_statistics = ngram_hash(ng_list,ngrams_statistics)
		line=fin.readline()
	ngrams_statistics_sorted = sorted(ngrams_statistics.items(), key=operator.itemgetter(1), reverse=True) [0:400]
	fin.close()
	return ngrams_statistics_sorted

def ngram_hash(ng_list, ngrams_statistics):
	for ngram in ng_list:
		if ngram not in ngrams_statistics:
			ngrams_statistics.update({ngram:1})
		else:
			ngram_occurrences = ngrams_statistics[ngram]
			ngrams_statistics.update({ngram:ngram_occurrences+1})
	return ngrams_statistics


def compare_ng_prof(lang_profile, word_profile):
    
    word_distance = 0
    
    lang_ngrams_sorted = [ngram[0] for ngram in lang_profile]
    word_ngrams_sorted = [ngram[0] for ngram in word_profile]
    
    maximum_out_of_place_value = len(lang_ngrams_sorted)
    
    for ngram in word_ngrams_sorted:
        word_index = word_ngrams_sorted.index(ngram)
        try:
            lang_profile_index = lang_ngrams_sorted.index(ngram)
        except ValueError:
            lang_profile_index = maximum_out_of_place_value
        
        distance = abs(lang_profile_index-word_index) # absolute value
        word_distance+=distance
    
    return word_distance