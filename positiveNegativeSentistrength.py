import csv
import codecs

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/posTags/'
DICTDIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/SentStrength_Data_Sept2011/'

dataFiles = [	'sarcasmpos',
				'notsarcasmpos']

Highly = ["A", "V", "R"]

positive = []
negative = []

with open(DICTDIR + 'EmotionLookupTable.txt', 'rb') as f:
	for line in f:
		X = line.split('\t')
		if int(X[1]) < 0:
			if X[0][len(X[0])-1] == "*":
				list2 = list(X[0])
				list3 = list2[:-1]
				negative.append(''.join(list3))
			else:
				negative.append(X[0])
		if int(X[1]) > 0:
			if X[0][len(X[0])-1] == "*":
				list2 = list(X[0])
				list3 = list2[:-1]
				positive.append(''.join(list3))
			else:
				positive.append(X[0])

positive = set(positive)
negative = set(negative)

#print positive
#print negative

for dataFile in dataFiles:
	print dataFile
	ct = 0
	final = []
	ll = []
	lines = [line for line in codecs.open(DATADIR + dataFile + ".txt", encoding="utf-8")]
	pw = 0
	PW = 0
	nw = 0
	NW = 0
	for line in lines:
		ct += 1
		if ct %1000 == 0:
			print ct
		if line != '\n':
			l = line.split('\t')
			for j in xrange(1,len(l[0])+1):
				prefix = l[0][:j]
				if prefix in positive:
					if l[1] in Highly:
						PW += 1
					pw += 1
					break
				if prefix in negative:
					if l[1] in Highly:
						NW += 1
					nw += 1
					break
				#print [pw,PW,nw,NW]
		else:
			final.append([pw,PW,nw,NW])
			pw = 0
			PW = 0
			nw = 0
			NW  = 0
	with open(DATADIR + dataFile + "posnegsentimentlinewise" ".csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(final)