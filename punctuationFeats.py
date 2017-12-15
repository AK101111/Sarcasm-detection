import csv

DATADIR = '/Users/nitishagarwal/Desktop/StatNLP/Project/Sarcasm-Detection/data/clean/'
dataFile = 'sarcasmcleaned.txt'

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

#Ibanez

def countHappyEmoticonFeats(dataPt, happyEmoticons):
	return [dataPt.count(happyEmoticon) for happyEmoticon in happyEmoticons]

def countFunnyEmoticonFeats(dataPt, funnyEmoticons):
	return [dataPt.count(funnyEmoticon) for funnyEmoticon in funnyEmoticons]

def countLikeEmoticonFeats(dataPt, likeEmoticons):
	return [dataPt.count(likeEmoticon) for likeEmoticon in likeEmoticons]

def countWonderEmoticonFeats(dataPt, wonderEmoticons):
	return [dataPt.count(wonderEmoticon) for wonderEmoticon in wonderEmoticons]

def countNegativeEmoticonFeats(dataPt, negativeEmoticons):
	return [dataPt.count(negativeEmoticon) for negativeEmoticon in negativeEmoticons]

def countOtherEmoticonFeats(dataPt, otherEmoticons):
	return [dataPt.count(otherEmoticon) for otherEmoticon in otherEmoticons]

with open(DATADIR + dataFile, 'rb') as csvfile:
	feats = []
	reader = csv.reader(csvfile, delimiter = ',')
	ct = 0
	for row in reader:
		#print row[0]
		feat = countPunctuationFeats(row[0], ['?', '!', '.', ',', '"', "'"])
		feat.append(countAllCaps(row[0]))
		feat.append(countVowelRepeat(row[0]))
		feat.append(len(row[0].split()))
		feat.append(countHappyEmoticonFeats(row[0], ['😃', '😀', '🙃', '😊', '😀', '😇']))
		feat.append(countFunnyEmoticonFeats(row[0], ['😂', '🤣', '😝', '😜', '😋', '😛', '😁']))
		feat.append(countLikeEmoticonFeats(row[0], ['👍', '😍', '😻', '💕', '💞', '❤', '💖', '💓', '👌']))
		feat.append(countWonderEmoticonFeats(row[0], ['😮', '😯', '😲', '🤔', '😳', '🙄', '🤷']))
		feat.append(countNegativeEmoticonFeats(row[0], ['😭', '😠', '😫', '😩', '😔', '😪', '😢', '😰', '😱', '🖕', '💔']))
		feat.append(countOtherEmoticonFeats(row[0], ['😅', '😎', '😏', '😒', '😐', '🙄', '😕', '😬', '😉', '😷', '👊', '🙌', '🙏', '👏', '🔥', '✨', '🙈', '🎃', '👻', '💀', '💩']))
		feats.append(feat)
	print(feats)
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