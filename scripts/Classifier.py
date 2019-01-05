from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

DATADIR = '/Users/arnavkansal/Desktop/logs/temp/Sarcasm-detection/fdata/'

file11 = 'joshi3M'
file10 = 'Njoshi3M'
file21 = 'pwnw'
file20 = 'Npwnw'
file31 = 'hack'
file30 = 'Nhack'
file41 = 'sentiLSTM'
file40 = 'NsentiLSTM'
file51 = 'posLSTM'
file50 = 'NposLSTM'

training_sarcastic = 50000
training_non_sarcastic = 50000

X_train11 = genfromtxt(DATADIR + file11 + '.csv', delimiter = ',')	#Features for sarcastic training dataset
X_train10 = genfromtxt(DATADIR + file10 + '.csv', delimiter = ',')	#Features for non-sarcastic training dataset
X_train21 = genfromtxt(DATADIR + file21 + '.csv', delimiter = ',')	#Features for sarcastic training dataset
X_train20 = genfromtxt(DATADIR + file20 + '.csv', delimiter = ',')	#Features for non-sarcastic training dataset
X_train31 = genfromtxt(DATADIR + file31 + '.csv', delimiter = ',')	#Features for sarcastic training dataset
X_train30 = genfromtxt(DATADIR + file30 + '.csv', delimiter = ',')	#Features for non-sarcastic training dataset
X_train41 = genfromtxt(DATADIR + file41 + '.csv', delimiter = ',')	#Features for sarcastic training dataset
X_train40 = genfromtxt(DATADIR + file40 + '.csv', delimiter = ',')	#Features for non-sarcastic training dataset
X_train51 = genfromtxt(DATADIR + file51 + '.csv', delimiter = ',')	#Features for sarcastic training dataset
X_train50 = genfromtxt(DATADIR + file50 + '.csv', delimiter = ',')	#Features for non-sarcastic training dataset
X_train1 = np.concatenate((X_train11, X_train21, X_train31, X_train41, X_train51), axis = 1)
X_train0 = np.concatenate((X_train10, X_train20, X_train30, X_train40, X_train50), axis = 1)
X_train = np.concatenate((X_train1[0 : training_sarcastic], X_train0[0 : training_non_sarcastic]))
X_test = np.concatenate((X_train1[training_sarcastic : X_train1.shape[0]], X_train0[training_non_sarcastic : X_train0.shape[0]]))
Y = [1] * training_sarcastic + [0] * training_non_sarcastic			#True Labels 1 for sarcasm and 0 for plain text
Y_true = [1] * (X_train1.shape[0] - training_sarcastic) + [0] * (X_train0.shape[0] - training_non_sarcastic)

#clf = svm.SVC(kernel = 'rbf', gamma = 2, C = 1000.0)

clf = LinearSVC(random_state = 0)
clf.fit(X_train, Y)
Y_pred = clf.predict(X_test)										#Predicted Labels 1 for sarcasm and 0 for plain text
f_score = precision_recall_fscore_support(Y_true, Y_pred)
print(f_score)

#fignum = 1
#for kernel in ('linear', 'poly', 'rbf'):
	#clf = svm.SVC(kernel = kernel, gamma = 2)
	#clf.fit(X_train, Y_true)
	#plt.figure(fignum, figsize = (4, 3))
	#plt.clf()
	#plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s = 80, facecolors = 'none', zorder = 10, edgecolors = 'k')
	#plt.scatter(X_train[:, 0], X_train[:, 1], c = Y_true, zorder = 10, cmap = plt.cm.Paired, edgecolors = 'k')
	#plt.axis('tight')
	#x_min = -3
	#x_max = 3
	#y_min = -3
	#y_max = 3
	#XX, YY = np.mgrid[x_min : x_max : 200j, y_min : y_max : 200j]
	#Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
	# Put the result into a color plot
	#Z = Z.reshape(XX.shape)
	#plt.figure(fignum, figsize = (4, 3))
	#plt.pcolormesh(XX, YY, Z > 0, cmap = plt.cm.Paired)
	#plt.contour(XX, YY, Z, colors = ['k', 'k', 'k'], linestyles = ['--', '-', '--'], levels = [-.5, 0, .5])
	#plt.xlim(x_min, x_max)
	#plt.ylim(y_min, y_max)
	#plt.xticks(())
	#plt.yticks(())
	#fignum = fignum + 1
	#y_pred = clf.predict(X_test)	#Predicted Labels 1 for sarcasm and 0 for plain text
	#precision_recall_fscore_support(y_true, y_pred)
plt.show()
