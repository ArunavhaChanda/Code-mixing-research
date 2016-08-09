from collections import defaultdict
import beng_search as beng
import re
import enchant
import arff
import lang_prof as ng
from nltk.corpus import brown
from nltk.tokenize import RegexpTokenizer
import eng_search as eng
from nltk.util import ngrams
import sys
import operator


def main():
	lno=1
	word_tot=0
	corr=0
	init_corr=0
	beng_statistics = {}
	beng_statistics = ng.ngram_prof("./beng_train.txt",beng_statistics)
	eng_statistics = {}

	'''	
	text = " ".join(brown.words())
	tokenizer = RegexpTokenizer("[a-zA-Z'`]+")
	text = tokenizer.tokenize(text)
	text = " ".join(text)
	brown_words=open("./brown_words.txt",'w')
	brown_words.write(text)
	brown_words.close()
	'''

	eng_statistics = ng.ngram_prof("./brown_words.txt",eng_statistics)

	lang_stats={}
	lang_stats.update({'e':eng_statistics})
	lang_stats.update({'b':beng_statistics})


	#fin=open("./beng_corpus.txt",'r')
	fin=open("./BanglaEnglish_FIRE2013_AnnotatedDev.txt",'r')
	#fout_pred=open("./predicted_tags_arff.txt",'w')
	#fout_corr=open("./corrected_tags_arff.txt",'w')
	word_list=[]
	eng_dic=[]
	beng_dic=[]
	ngram=[]
	surround=[]
	corr_tag=[]
	data=[]
	sent=fin.readline()
	while(sent):
		############ Only for Facebook corpus (COMMENT for FIRE)
		#sent = re.sub(r'[^\w\s]','',sent)
		##########################################
		words=[]
		sent=sent.split()
		for elem in sent:
			############ Only for FIRE CORPUS (COMMENT for Facebook)
			elem=elem.split('\\')
			corr_tag.append(elem[1][0])
			elem=elem[0]
			#################################
			elem.strip()
			words.append(elem)
		type_map = defaultdict(str)
		type_count = defaultdict(int)
		word_count=0

		for word in words:
			word=word.strip(" ")
			word_list.append(word)
			word_count+=1
			beng_rat=0
			eng_rat=0
			if(beng.beng_word(word)):
				beng_rat=1
			if(eng.eng_search(word)):
				eng_rat=1

			eng_dic.append(eng_rat)
			beng_dic.append(beng_rat)

			word_statistics={}
			lang_ratio = {}

			grams = ngrams(word,4,pad_left=True,pad_right=True,left_pad_symbol=' ',right_pad_symbol=' ')
			grams=list(grams)
			ng_list=[]
			for j in range (len(grams)):
				ng_list.append(''.join(grams[j]))
			word_statistics = ng.ngram_hash(ng_list,word_statistics)
			word_statistics = sorted(word_statistics.items(), key=operator.itemgetter(1), reverse=True)
			for lang, ngrams_statistics in lang_stats.items():
				distance = ng.compare_ng_prof(ngrams_statistics,word_statistics)
				lang_ratio.update({lang:distance})
			ng_lang_result = min(lang_ratio, key = lang_ratio.get).upper()

			ngram.append(ng_lang_result)

			if(beng_rat and not eng_rat):
				type_word="Bengali word"
			elif(eng_rat and not beng_rat):
				type_word="English word"
			else:
				if(ng_lang_result=='B'):
					type_word="Bengali word"
				else:
					type_word="English word"

			type_map[word]=type_word
			type_count[type_word]+=1

			#print(str(word)+"(Detect:"+str(type_map[word])+")")
			
		if((type_count["English word"])>(type_count["Bengali word"])):
			default="e"
		else:
			default="b"
		print(str(lno)+default)
		lno+=1
		for i in range(len(words)):
			word_count=0
			type_count["English word"]=0
			type_count["Bengali word"]=0

			if(i>1 and i<(len(words)-2)):
				word_count=4
				for j in range(i-2,min((len(words)-1),(i+3))):
					if(j!=i):
						type_count[type_map[words[j]]]+=1
			elif (i<=1):
				word_count=min(i+2,len(words)-1)
				for j in range(min((len(words)-1),(i+3))):
					if(j!=i):
						type_count[type_map[words[j]]]+=1
			elif(i>=(len(words)-2)):
				word_count= (len(words)-i)+1
				for j in range(i-2,len(words)):
					if(j!=i):
						type_count[type_map[words[j]]]+=1
			if(word_count):
				surround.append(str(type_count["Bengali word"]/word_count))
				#if((type_count["Bengali word"]/word_count)>=0.5):
				#	surround.append('1')
				#else:
				#	surround.append('0')
			else:
				surround.append('0')
		sent=fin.readline()

	
	############ Only for Facebook corpus (COMMENT for FIRE)
	#real_tag = open("./real_tags.txt",'r')
	#line = real_tag.readline().split()
	#for word in line:
	#	tags=word.split('\\')
	#	corr_tag.append(tags[1])
	#real_tag.close()
	######################################
	

	for i in range(len(word_list)):
		vector=[]
#		vector.append(word_list[i])
		vector.append(int(eng_dic[i]))
		vector.append(int(beng_dic[i]))
		vector.append(ngram[i])
		vector.append(float(surround[i]))
		vector.append(corr_tag[i])
		data.append(vector)

	obj={
	'description': u'',
	'relation': 'langid',
	'attributes': [
	('eng_dict','NUMERIC'),
	('beng_dict','NUMERIC'),
	('ngram','STRING'),
	('beng_surr','REAL'),
	('real_tag','STRING')
	],
	'data':data,

	}

	final = arff.dumps(obj)

	#FIRE
	final_file=open("./lang_id_fire.arff",'w')
	#
	#Facebook
	#final_file=open("./lang_id.arff",'w')
	#
	final_file.write(final)
	final_file.close()

	fin.close()
#	fout_pred.close()
#	fout_corr.close()

main()