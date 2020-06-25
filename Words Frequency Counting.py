import pandas as pd 
import numpy as np import nltk
import xlwt
  
review = pd.read_excel('bestblower.xlsx')   
for i in range(len(review['review_body'])):
  sentence = review['rreview_body'][i]
  review['rreview_body'][i] = nltk.word_tokenize(sentence)
train = pd.concat([review['rreview_body'][i]], ignore_index = True)   
  
word = [] 
for i in train:  
  word.extend(i)  
dict=pd.Series(w).value_counts()
a=dict.keys()
 
for i in range(len(a)):
print(a[i])
