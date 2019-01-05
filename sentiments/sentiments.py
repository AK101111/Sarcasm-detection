from nltk import word_tokenize
from nltk.corpus import sentiwordnet as swn
import csv
import codecs

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/posTags/'
dataFiles = [	'sarcasmpos',
				'notsarcasmpos']

NOUNS = ["N", "O", "S", "^", "Z", "L", "M"]

def convertPos(posTag):
	if posTag in NOUNS:
		return "n"
	if posTag == "A":
		return "a"
	if posTag == "R":
		return "r"
	if posTag == "V":
		return "v"
	return "z"

def score(word, posTag):
	if posTag == "z":
		scoress = [swn.senti_synsets(word, pos) for pos in ["a", "s", "r", "n", "v"]]
		for scores in scoress:
			pos=0
			neg=0
			for synst in scores:
				pos += synst.pos_score()
				neg += synst.neg_score()
			return 1-(pos+neg)
		return 0.5		
	
	scores = swn.senti_synsets(word, posTag)
	pos=0
	neg=0
	for synst in scores:
		pos += synst.pos_score()
		neg += synst.neg_score()
	if pos == 0 and neg == 0:
		return 0.5
	return 1-(pos+neg)

for dataFile in dataFiles:
	print dataFile
	ct = 0
	final = []
	ll = []
	lines = [line for line in codecs.open(DATADIR + dataFile + ".txt", encoding="utf-8")]
	for line in lines:
		ct += 1
		if ct %1000 == 0:
			print ct
		if line != '\n':
			l = line.split('\t')
			ll.append(score(l[0], convertPos(l[1])))
		else:
			final.append(ll)
			ll = []
	with open(DATADIR + dataFile + "sentimentlinewise" ".csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(final)