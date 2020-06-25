import xlwt
import pandas as pd #导入Pandas  
import nltk

review = pd.read_excel('pacifier.xlsx') #读入评论内容   
for i in range(len(review['review_body'])):
sentence = review['review_body'][i]
review['solve'][i] = nltk.word_tokenize(sentence)

length=[]
for i in range(len(review['solve'])):
l=len(review['solve'][i])
length.append(l)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")
for i in range(len(length)):
    sheet.write(i,0,length[i])
workbook.save("test.xls")
