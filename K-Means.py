import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.cluster import KMeans
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('1.csv',header=None)
data.columns=['score','date']
features =  ['score','date']
X = data[features]
x=data['date']
y=data['score']

plt.title("B00SKQFT4I")
plt.xlabel("date")
plt.ylabel("score")
plt.style.use('fivethirtyeight')
plt.plot(x,y)

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))
plt.show()

sns.relplot(x="star",y="score",data=data)

km = KMeans(6)
km.fit(X)
data['cluster_k6'] = km.predict(X)
sns.relplot(x="star", y="score", hue="cluster_k6",palette="Set1",data=data)

param_test1 = {'n_clusters':np.arange(2,11,1)}
gsearch1 = GridSearchCV(estimator = KMeans(),param_grid = param_test1,cv=5)
gsearch1.fit(X)
score_list=-pd.DataFrame(gsearch1.cv_results_)['mean_test_score']
sns.lineplot(x=range(2,11),y=score_list)
