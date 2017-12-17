# hack
# hack + pwnw = Bouzizi
# joshi
# hack + joshi
# hack + pwnw + joshi
# pos
# senti
# pos + senti
# hack + pwnw + joshi + pos + senti

import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn import cross_validation, metrics   #Additional scklearn functions
from sklearn.grid_search import GridSearchCV   #Perforing grid search
from numpy import genfromtxt

hack = genfromtxt('fdata/hack.csv', delimiter = ',')
hackN = genfromtxt('fdata/Nhack.csv', delimiter = ',')

hackTrain = hack[:50000]
hackNTrain = hackN[:50000]
hackTest = hack[50000:]
hackNTest = hackN[50000:]

pwnw = genfromtxt('fdata/pwnw.csv', delimiter = ',')
pwnwN = genfromtxt('fdata/Npwnw.csv', delimiter = ',')

pwnwTrain = pwnw[:50000]
pwnwNTrain = pwnwN[:50000]
pwnwTest = pwnw[50000:]
pwnwNTest = pwnwN[50000:]

joshi = genfromtxt('fdata/joshi3M.csv', delimiter = ',')
joshiN = genfromtxt('fdata/Njoshi3M.csv', delimiter = ',')

joshiTrain = joshi[:50000]
joshiNTrain = joshiN[:50000]
joshiTest = joshi[50000:]
joshiNTest = joshiN[50000:]

pos = genfromtxt('fdata/posLSTM.csv', delimiter = ',')
posN = genfromtxt('fdata/NposLSTM.csv', delimiter = ',')

posTrain = pos[:50000]
posNTrain = posN[:50000]
posTest = pos[50000:]
posNTest = posN[50000:]

senti = genfromtxt('fdata/sentiLSTM.csv', delimiter = ',')
sentiN = genfromtxt('fdata/NsentiLSTM.csv', delimiter = ',')

sentiTrain = senti[:50000]
sentiNTrain = sentiN[:50000]
sentiTest = senti[50000:]
sentiNTest = sentiN[50000:]

dataITrain= np.concatenate((hackTrain,hackNTrain), axis=0)
dataIITrain = np.concatenate((pwnwTrain,pwnwNTrain), axis=0)
dataIIITrain= np.concatenate((joshiTrain,joshiNTrain), axis=0)
dataIVTrain = np.concatenate((posTrain,posNTrain), axis=0)
dataVTrain = np.concatenate((sentiTrain,sentiNTrain), axis=0)

dataITest= np.concatenate((hackTest,hackNTest), axis=0)
dataIITest = np.concatenate((pwnwTest,pwnwNTest), axis=0)
dataIIITest= np.concatenate((joshiTest,joshiNTest), axis=0)
dataIVTest = np.concatenate((posTest,posNTest), axis=0)
dataVTest = np.concatenate((sentiTest,sentiNTest), axis=0)

trains = [ dataITrain, np.concatenate((dataITrain, dataIITrain), axis = 1), dataIIITrain, np.concatenate((dataITrain, dataIIITrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain), axis = 1), dataIVTrain, dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ np.concatenate((dataITrain, dataIITrain), axis = 1), dataIIITrain, np.concatenate((dataITrain, dataIIITrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain), axis = 1), dataIVTrain, dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ dataIIITrain, np.concatenate((dataITrain, dataIIITrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain), axis = 1), dataIVTrain, dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ np.concatenate((dataITrain, dataIIITrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain), axis = 1), dataIVTrain, dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ np.concatenate((dataITrain, dataIITrain, dataIIITrain), axis = 1), dataIVTrain, dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ dataIVTrain, dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ dataVTrain, np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ np.concatenate((dataIVTrain, dataVTrain), axis = 1), np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
# trains = [ np.concatenate((dataITrain, dataIITrain, dataIIITrain, dataIVTrain, dataVTrain), axis = 1)]
y_train = np.array([1]*len(hackTrain) + [0]*len(hackNTrain))

tests = [dataITest, np.concatenate((dataITest, dataIITest), axis = 1), dataIIITest, np.concatenate((dataITest, dataIIITest), axis = 1), np.concatenate((dataITest, dataIITest, dataIIITest), axis = 1), dataIVTest, dataVTest, np.concatenate((dataIVTest, dataVTest), axis = 1), np.concatenate((dataITest, dataIITest, dataIIITest, dataIVTest, dataVTest), axis = 1)]

y_test = np.array([1]*len(hackTest) + [0]*len(hackNTest))

param_test2 = {
 'max_depth':[4,5,6,7,8,9,10]
}

gsearches = []
for i in range(1):
	print i
	print "started"
	gsearch = GridSearchCV(estimator = XGBClassifier( learning_rate=0.1,n_estimators=100, max_depth=5,min_child_weight=2,gamma=0,subsample=0.8,colsample_bytree=0.8,objective= 'binary:logistic',nthread=4, scale_pos_weight=1,	seed=27), param_grid = param_test2, scoring='roc_auc',n_jobs=4,iid=False, cv=5) 
	gsearches.append(gsearch)
	gsearches[0].fit(trains[i], y_train)
	gsearches[0].grid_scores_, gsearches[0].best_params_, gsearches[0].best_score_
	print "done"
	print i

y_score = gsearches[0].predict(tests[8])

p1 = (np.dot(y_score, y_test))/ (np.linalg.norm(y_score)**2)
r1 = (np.dot(y_score, y_test))/ (np.linalg.norm(y_test)**2)
p0 = (np.dot(1-np.array(y_score), 1-np.array(y_test)))/ (np.linalg.norm(1-np.array(y_score))**2)
r0 = (np.dot(1-np.array(y_score), 1-np.array(y_test)))/ (np.linalg.norm(1-np.array(y_test))**2)
print [p1,r1,p0,r0]