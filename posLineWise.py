import csv
import re
import string
import preprocessor

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/posTags/'
dataFiles = [	'sarcasm1031', 
				'sarcasm1205', 
				'sarcastic1031', 
				'sarcastic1205']

for dataFile in dataFiles:
	final = []
	ll= []
	lines = [line for line in open(DATADIR + dataFile + ".txt")]
	for line in lines:
		if line != '\n':
			ll.append(line.split('\t')[1])
		else:
			final.append(ll)
			ll = []
	with open(DATADIR + dataFile + ".csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(final)