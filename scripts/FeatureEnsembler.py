import csv
import re
import string

DATADIR = '/Users/arnavkansal/Desktop/logs/temp/Sarcasm-detection/Data'


Files = [	'#sarcasm_since_2013-10-01_until_2017-10-31',
		'#sarcasm_since_2017-10-31_until_2017-12-05',
		'#sarcastic_since_2013-10-01_until_2017-10-31',
		'#sarcastic_since_2017-10-31_until_2017-12-05']

Features = ['cleaned', 'POS']
Data_Features = [[]]

for File in Files:
	Data_Features1 = [[]]
	for Feature in Features:
		Data_Features2 = [[]]
		with open(DATADIR + File + Feature + ".csv", 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter = ' ')
			for row in reader:
				DataFeatures = DataFeatures + row

with open(DATADIR + dataFile + "Features.csv",'wb') as resultFile:
	wr = csv.writer(resultFile)
	wr.write([Data_Features])
