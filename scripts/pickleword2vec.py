# coding: utf-8
from __future__ import division

import struct
import sys
import csv

FILE_NAME = "wordvec/GoogleNews-vectors-negative300.bin"
MAX_VECTORS = 300000
FLOAT_SIZE = 4 # 32bit float

vectors = dict()

with open(FILE_NAME, 'rb') as f:
    c = None
    # read the header
    header = ""
    while c != "\n":
        c = f.read(1)
        header += c

    total_num_vectors, vector_len = (int(x) for x in header.split())
    num_vectors = min(MAX_VECTORS, total_num_vectors)
    
    print "Number of vectors: %d/%d" % (num_vectors, total_num_vectors)
    print "Vector size: %d" % vector_len

    while len(vectors) < num_vectors:

        word = ""        
        while True:
            c = f.read(1)
            if c == " ":
                break
            word += c

        binary_vector = f.read(FLOAT_SIZE * vector_len)
        vectors[word] = [ struct.unpack_from('f', binary_vector, i)[0] 
                          for i in xrange(0, len(binary_vector), FLOAT_SIZE) ]
        
        sys.stdout.write("%d%%\r" % (len(vectors) / num_vectors * 100))
        sys.stdout.flush()

DATADIR = '/Users/arnavkansal/Desktop/Courant/Fall17/StatNLP/Sarcasm/data/clean/'
dataFiles = [   'sarcasmcleaned',
                'notsarcasmcleaned']

import nltk
import random
import numpy as np
import codecs

rand_v = [random.random() for i in range(300)]

from scipy import spatial

for dataf in dataFiles:
    ll = []
    with codecs.open(DATADIR + dataf + ".txt", encoding="utf-8") as f:
        ct = 0
        for line in f:
            if ct % 1000 == 0:
                sys.stdout.write("%d\r" % ct)
                sys.stdout.flush()
            ct += 1
            tokenized = nltk.word_tokenize(line)
            Sim = np.zeros((len(tokenized), len(tokenized)))
            for i in range(len(tokenized)):
                for j in range(len(tokenized)):
                    if i != j:
                        if tokenized[i] in vectors:
                            dataSetI = vectors[tokenized[i]]
                        else:
                            dataSetI = rand_v
                        if tokenized[j] in vectors:
                            dataSetII = vectors[tokenized[j]]
                        else:
                            dataSetI = rand_v    
                        Sim[i][j] = 1 - spatial.distance.cosine(dataSetI, dataSetII)
                    else:
                        Sim[i][j] = 0
            rowMaxMax = -1000000
            rowMaxMin = 1000000
            rowMinMax = -1000000
            rowMinMin = 1000000
            for i in range(len(tokenized)):
                rowMax = -100000
                rowMin = 100000
                for j in range(len(tokenized)):
                    if i != j:
                        rowMax = max(rowMax,Sim[i][j])
                        rowMin = min(rowMin,Sim[i][j])
                rowMaxMax = max(rowMaxMax, rowMax)
                rowMaxMin = min(rowMaxMin, rowMax)
                rowMinMax = max(rowMinMax, rowMin)
                rowMinMin = min(rowMinMin, rowMin)
            SimI = np.zeros((len(tokenized), len(tokenized)))
            for i in range(len(tokenized)):
                for j in range(len(tokenized)):
                    if i != j:
                        Sim[i][j] = Sim[i][j]/((i-j)*(i-j))
                    else:
                        SimI[i][j] = 0
            rowMaxMaxI = -1000000
            rowMaxMinI = 1000000
            rowMinMaxI = -1000000
            rowMinMinI = 1000000
            for i in range(len(tokenized)):
                rowMax = -100000
                rowMin = 100000
                for j in range(len(tokenized)):
                    if i != j:
                        rowMax = max(rowMax,Sim[i][j])
                        rowMin = min(rowMin,Sim[i][j])
                rowMaxMaxI = max(rowMaxMaxI, rowMax)
                rowMaxMinI = min(rowMaxMinI, rowMax)
                rowMinMaxI = max(rowMinMaxI, rowMin)
                rowMinMinI = min(rowMinMinI, rowMin)
            ll.append([rowMaxMax, rowMaxMin, rowMinMax, rowMinMin, rowMaxMaxI, rowMaxMinI, rowMinMaxI, rowMinMinI])    
    with open(DATADIR + dataf + "vecs.txt", 'wb') as ff:
        writer = csv.writer(ff)
        writer.writerows(ll)