from sklearn import svm
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from numpy import genfromtxt

DATADIR = '/Users/nitishagarwal/Desktop/StatNLP/Project/Sarcasm-detection/vector_rep/'
file1 = 'sarcasmcleanedvecs300000-300'
file0 = 'notsarcasmcleanedvecs30000-300'

X_train1 = genfromtxt(DATADIR + file1 + '.csv', delimiter = ',')	#Features for sarcastic training dataset
X_train0 = genfromtxt(DATADIR + file0 + '.csv', delimiter = ',')	#Features for non-sarcastic training dataset
X_train = np.concatenate((X_train1, X_train0))
X_test = []															#Features for test dataset
Y_true = [1] * X_train1.shape[0] + [0] * X_train0.shape[0]			#True Labels 1 for sarcasm and 0 for plain text

clf = svm.SVC(kernel = 'rbf', gamma = 2)
clf.fit(X_train, Y_true)


#fignum = 1
#for kernel in ('linear', 'poly', 'rbf'):
#	clf = svm.SVC(kernel = kernel, gamma = 2)
#	clf.fit(X_train, Y_true)
#	plt.figure(fignum, figsize = (4, 3))
#	plt.clf()
#	X_test
#	plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s = 80, facecolors = 'none', zorder = 10, edgecolors = 'k')
#	plt.scatter(X[:, 0], X[:, 1], c = Y, zorder = 10, cmap = plt.cm.Paired, edgecolors = 'k')
#	plt.axis('tight')
#	x_min = -3
#	x_max = 3
#	y_min = -3
#	y_max = 3
#	XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
#	Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
	# Put the result into a color plot
#	Z = Z.reshape(XX.shape)
#	plt.figure(fignum, figsize=(4, 3))
#	plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
#	plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'], levels=[-.5, 0, .5])
#	plt.xlim(x_min, x_max)
#	plt.ylim(y_min, y_max)
#	plt.xticks(())
#	plt.yticks(())
#	fignum = fignum + 1
	#y_pred = clf.predict(X_test)	#Predicted Labels 1 for sarcasm and 0 for plain text
	#precision_recall_fscore_support(y_true, y_pred)
#plt.show()