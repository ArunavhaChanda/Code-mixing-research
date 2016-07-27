real=open("./real_tags.txt",'r')
pred=open("./predicted_tags_eng.txt",'r')
corr=open("./corrected_tags_eng.txt",'r')

rline=real.readline().split()
pline=pred.readline().split()
cline=corr.readline().split()

words=0
pright=0
cright=0

for i in range(len(rline)):
	rpair=rline[i].split('\\')
	ppair=pline[i].split('\\')
	cpair=cline[i].split('\\')
	if(rpair[1]==ppair[1]):
		pright+=1
	if(rpair[1]==cpair[1]):
		cright+=1
	words+=1

print("Total words: "+str(words))
print("Predictor accuracy: "+str((pright*100)/words)+"%")
print("Corrector accuracy: "+str((cright*100)/words)+"%")