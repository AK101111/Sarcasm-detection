import csv
import re
import string
import preprocessor

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

dataSarcasm = []
dataTotal = []

def strip_links(text):
    link_regex    = re.compile('((http?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

preprocessor.set_options(preprocessor.OPT.URL, preprocessor.OPT.HASHTAG, preprocessor.OPT.MENTION)
def findClean(dataPt, switch):
	if switch:
		return preprocessor.clean(dataPt)
		#return strip_all_entities(strip_links(dataPt))
		#return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",strip_all_entities(dataPt)).split())
	else:
		if dataPt.find("#sarcasm") == -1 and dataPt.find("#sarcastic") == -1:
			return None
		else:
			return preprocessor.clean(dataPt)
			#return strip_all_entities(strip_links(dataPt))
			#return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",strip_all_entities(dataPt)).split())

for dataFile in dataFilesI:
	with open(DATADIR + dataFile + ".csv", 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		ct = 0
		for row in reader:
			# skip header
			# ['id', 'screen_name', 'utc_offset', 'description', 'location', 'created_at', 'text', 'retweet_count', 'favorite_count']
			if(ct == 0):
				ct += 1
				continue
			# if description field contains "sarcasm" or "sarcastic" clean it (remove #hashtag) and add it to data
			# print row[3]
			# print row[6]
			cleanData = findClean(row[3],False)
			# clean description feild (remove #hashtag) and add it to data
			cleanDataI = findClean(row[3],True)
			if cleanData:
				dataSarcasm.append(cleanData)
			if cleanDataI:
				dataTotal.append(cleanDataI)
			
			# if text field contains "sarcasm" or "sarcastic" clean it (remove #hashtag) and add it to data
			cleanData = findClean(row[6],False)
			# clean text field (remove #hashtag) and add it to data
			cleanDataI = findClean(row[6],True)
			if cleanData:
				dataSarcasm.append(cleanData)
			if cleanDataI:
				dataTotal.append(cleanDataI)
		
		with open(DATADIR + dataFile + "cleaned.txt",'wb') as textfile:
			for sentences in dataSarcasm:
  				textfile.write("%s\n" % sentences)

		with open(DATADIR + dataFile + "cleaned.csv",'wb') as resultFile:
			wr = csv.writer(resultFile)
			for sentences in dataSarcasm:
				wr.writerow([sentences])
