#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
import codecs

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm-detection/'
dataFiles = ['sarcasmcleaned','notsarcasmcleaned']

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

for dataFile in dataFiles:
	feats = []
	with codecs.open(DATADIR + "data/clean/" + dataFile + ".txt", encoding="utf-8") as csvfile:	
		ct = 0
		for row in csvfile:
			ct += 1
			feat = countPunctuationFeats(row, ['?', '!', '.', ',', '"', "'"])
			feat.append(countAllCaps(row))
			feat.append(countVowelRepeat(row))
			feat.append(len(row.split()))
			feat += [sum(countHappyEmoticonFeats(row, ['😃', '😀', '🙃', '😊', '😀', '😇']))]
			feat += [sum(countFunnyEmoticonFeats(row, ['😂', '🤣', '😝', '😜', '😋', '😛', '😁']))]
			feat += [sum(countLikeEmoticonFeats(row, ['👍', '😍', '😻', '💕', '💞', '❤', '💖', '💓', '👌']))]
			feat += [sum(countWonderEmoticonFeats(row, ['😮', '😯', '😲', '🤔', '😳', '🙄', '🤷']))]
			feat += [sum(countNegativeEmoticonFeats(row, ['😭', '😠', '😫', '😩', '😔', '😪', '😢', '😰', '😱', '🖕', '💔']))]
			feat += [sum(countOtherEmoticonFeats(row, ['😅', '😎', '😏', '😒', '😐', '🙄', '😕', '😬', '😉', '😷', '👊', '🙌', '🙏', '👏', '🔥', '✨', '🙈', '🎃', '👻', '💀', '💩']))]
			feats.append(feat)
		print ct
		print len(feats)
	with open(DATADIR + "hackyfeats/" + dataFile + "hackfeats.csv",'wb') as fii:    
		wr = csv.writer(fii)
		wr.writerows(feats)