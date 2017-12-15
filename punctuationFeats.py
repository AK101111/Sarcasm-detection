import csv

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/twitter-to-csv-master/'
dataFiles = [	'#ironical_since_2013-10-01_until_2017-10-31', 
				'#ironical_since_2017-10-31_until_2017-12-05', 
				'#irony_since_2013-10-01_until_2017-10-31',
				'#irony_since_2017-10-31_until_2017-12-05' ,
				'#sarcasm_since_2013-10-01_until_2017-10-31', 
				'#sarcasm_since_2017-10-31_until_2017-12-05',
				'#sarcastic_since_2013-10-01_until_2017-10-31', 
				'#sarcastic_since_2017-10-31_until_2017-12-05']
dataFilesI = [	'#sarcasm_since_2013-10-01_until_2017-10-31', 
				'#sarcasm_since_2017-10-31_until_2017-12-05',
				'#sarcastic_since_2013-10-01_until_2017-10-31', 
				'#sarcastic_since_2017-10-31_until_2017-12-05']

# punctutation may be 
# ?, !, ., ", '
def countPunctuationFeats(dataPt, punctuations):
	return [dataPt.count(punctuation) for punctuation in punctuations]

def countAllCaps(dataPt):
	count = 0
	for word in dataPt.split():
		done = True
		for ch in word:
			if not ch.isupper():
				done = False
				break
		if done:
			count += 1
	return count

def countVowelRepeat(dataPt):
	count = 0
	vowels = ['a','e','i','o','u']
	for word in dataPt.split():
		done = True
		prev = None
		for ch in word:
			if ch in vowels:
				if not prev:
					prev = ch
				else:
					if prev == ch:
						count += 1
			else:
				prev = None
	return count

def sentimentFeats(dataPt):
	return None

def 

for dataFile in dataFilesI:
	with open(DATADIR + dataFile + "cleaned.txt", 'rb') as csvfile:
		feats = []
		reader = csv.reader(csvfile, delimiter=',')
		ct = 0
		for row in reader:
			#print row[0]
			feat = countPunctuationFeats(row[0], ['?', '!', '.', ',', '"', "'"])
			feat.append(countAllCaps(row[0]))
			feat.append(countVowelRepeat(row[0]))
			feat.append(len(row[0].split()))
			feats.append(feat)
		#for feat in feats:
		#	print(feat)
		

		#write feats to file

		# with open(DATADIR + dataFile + "cleaned.txt",'wb') as textfile:
		# 	for sentences in dataSarcasm:
  		# 		textfilels.write("%s\n" % sentences)

		# with open(DATADIR + dataFile + "cleaned.csv",'wb') as resultFile:
		# 	wr = csv.writer(resultFile)
		# 	for sentences in dataSarcasm:
		# 		wr.writerow([sentences])
