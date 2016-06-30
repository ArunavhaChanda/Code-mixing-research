import requests
from bs4 import BeautifulSoup

def eng_word(word):
	url = 'http://wordnetweb.princeton.edu/perl/webwn?s='+word+'&sub=Search+WordNet&o2=&o0=1&o7=&o5=&o1=1&o6=&o4=&o3=&h='
	response = requests.get(url)

	html=response.content

	soup = BeautifulSoup(html,"html.parser")

	result = soup.find('div',attrs={'class':'form'})

	if (result!=None):
		return 1
	else:
		engdict = open("./engcsv.csv",'r')
		line = engdict.readline().split(",")
		for stop in line:
			stop=stop.strip(" ")
			if(word.lower()==stop.lower()):
				engdict.close()
				return 1
	engdict.close()
	return 0
