import pandas as pd
import numpy as np
import nltk
from keras.preprocessing import sequence  
from keras.optimizers import SGD, RMSprop, Adagrad  
from keras.utils import np_utils  
from keras.models import Sequential  
from keras.layers.core import Dense, Dropout, Activation  
from keras.layers.embeddings import Embedding  
from keras.layers.recurrent import LSTM, GRU  
words = []

neg = pd.read_excel('negative.xlsx',header=None)  
pos = pd.read_excel('positive.xlsx',header=None)  
set1 = pd.concat([pos,neg],ignore_index=True)
neg_len = len(neg)  
pos_len = len(pos)
 
for i in range(len(set1[1])):
  sentence = set1[1][i]
  set[1][i] = nltk.word_tokenize(sentence)
  
set2 = pd.read_excel('reviews.xlsx') 
for i in range(len(set2['review_body'])):
  sentence = set2['review_body'][i]
  set2['review_body'][i] = nltk.word_tokenize(sentence)
  
set3 = pd.concat([set1[1], set2['review_body']], ignore_index = True)   
for i in set3:  
  words.extend(i)  
  
dict = pd.DataFrame(pd.Series(words).value_counts())
dict['id'] = list(range(1,len(dict)+1))  

get_sent = lambda x: list(dict['id'][x])  
set1['review_body'] = set1[1].apply(get_sent)   

maxlen = 50  

set1['review_body'] = list(sequence.pad_sequences(pn['sent'], maxlen=maxlen))
x_train = np.array(list(set1['review_body']))[::2]
y_train = np.array(list(set1['emotion']))[::2]  
x_test = np.array(list(set1['review_body']))[1::2] 
y_test = np.array(list(pn['emotion']))[1::2]  
x_full = np.array(list(set1['review_body'])) #全集  
y_full = np.array(list(set1['emotion']))  
  
model = Sequential()  
model.add(Embedding(len(dict)+1, 256))  
model.add(LSTM(256))model.add(Dropout(0.5))  
model.add(Dense(256))
model.add(Dense(128))
model.add(Dense(2)) 
model.add(Activation('sigmoid'))  
  
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])  
model.fit(x_full, y_full, batch_size=16, epochs=5) 
