import numpy as np
from sklearn.model_selection import train_test_split
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

vec = dict()
ct = 1

np.random.seed(7)
import csv
with open('posTags/sarcasmposlinewise.csv','rb') as f:
    reader = csv.reader(f)
    X_sar = list(reader)

#X_sar = [x for x in X_sar if len(x) < 40]

for i in range(len(X_sar)):
    for j in range(len(X_sar[i])):
        if X_sar[i][j] not in vec:
            vec[X_sar[i][j]] = ct
            X_sar[i][j] = ct
            ct += 1
        else:
            X_sar[i][j] = vec[X_sar[i][j]]

with open('posTags/notsarcasmposlinewise.csv','rb') as f:
    reader = csv.reader(f)
    X_Nsar = list(reader)

#X_Nsar = [x for x in X_Nsar if len(x) < 40]

for i in range(len(X_Nsar)):
    for j in range(len(X_Nsar[i])):
        if X_Nsar[i][j] not in vec:
            vec[X_Nsar[i][j]] = ct
            X_Nsar[i][j] = ct
            ct += 1
        else:
            X_Nsar[i][j] = vec[X_Nsar[i][j]]

y_sar = [1]*len(X_sar)
y_Nsar = [0]*len(X_Nsar)

X_tot = X_sar + X_Nsar
y_tot = y_sar + y_Nsar

X_sartrain, X_sartest, y_sartrain, y_sartest = train_test_split(X_sar, y_sar, test_size=0.1, random_state=1)
X_Nsartrain, X_Nsartest, y_Nsartrain, y_Nsartest = train_test_split(X_Nsar, y_Nsar, test_size=1-(0.9*len(X_sar)/len(X_Nsar)), random_state=1)

X_train = X_sartrain + X_Nsartrain
X_test = X_sartest + X_Nsartest
y_train = y_sartrain + y_Nsartrain
y_test = y_sartest + y_Nsartest

#from sklearn.utils import shuffle
#X_train, y_train = shuffle(X_train, y_train)

max_length = 30
X_train = sequence.pad_sequences(X_train, maxlen=max_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_length)

model = Sequential()
model.add(Embedding(25, 50, input_length=30))
model.add(LSTM(20, name = "LSTM"))
model.add(Dense(1, activation='sigmoid'))

import keras.backend as K

def f1_score(y_true, y_pred):
    # Count positive samples.
    c1 = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    c2 = K.sum(K.round(K.clip(y_pred, 0, 1)))
    c3 = K.sum(K.round(K.clip(y_true, 0, 1)))
    # If there are no true samples, fix the F1 score at 0.
    if c3 == 0:
        return 0
    # How many selected items are relevant?
    precision = c1 / c2
    # How many relevant items are selected?
    recall = c1 / c3
    # Calculate f1_score
    if precision + recall == 0:
    	return 0
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

#model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['binary_accuracy', f1_score])
print(model.summary())
model.fit(X_train, y_train, epochs=5, batch_size=128, verbose=1)

from keras.models import Model
layer_name = 'LSTM'
intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer(layer_name).output)

intermediate_output = intermediate_layer_model.predict(np.array(sequence.pad_sequences(X_sar, maxlen=max_length)))
intermediate_outputI = intermediate_layer_model.predict(np.array(sequence.pad_sequences(X_Nsar, maxlen=max_length)))
np.savetxt("posTags/possarcasticLSTM25-20.csv", intermediate_output, delimiter=",")
np.savetxt("posTags/posnonsarcasticLSTM25-20.csv", intermediate_outputI, delimiter=",")

# Final evaluation of the model
y_score = model.predict(X_test)
y_score = [int(round(u[0])) for u in y_score]

p1 = (np.dot(y_score, y_test))/ (np.linalg.norm(y_score)**2)
r1 = (np.dot(y_score, y_test))/ (np.linalg.norm(y_test)**2)
p0 = (np.dot(1-np.array(y_score), 1-np.array(y_test)))/ (np.linalg.norm(1-np.array(y_score))**2)
r0 = (np.dot(1-np.array(y_score), 1-np.array(y_test)))/ (np.linalg.norm(1-np.array(y_test))**2)

scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
