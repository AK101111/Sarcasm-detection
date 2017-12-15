import csv

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/posTags/'
dataFiles = [	'sarcasmpos',
				'notsarcasmpos']

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
	with open(DATADIR + dataFile + "linewise" ".csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(final)