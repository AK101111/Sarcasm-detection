from sklearn import svm
from sklearn.metrics import precision_recall_fscore_support
import numpy as np

X_train = []					#Features for training dataset
X_test = []						#Features for test dataset
y_true = np.array([])			#True Labels 1 for sarcasm and 0 for plain text

clf = svm.SVC()
clf.fit(X_train, y)

y_pred = clf.predict(X_test)	#Predicted Labels 1 for sarcasm and 0 for plain text

precision_recall_fscore_support(y_true, y_pred)