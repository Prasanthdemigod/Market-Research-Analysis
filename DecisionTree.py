'''

Implementing Decision Tree Classifier on the Dataset for predicting Business categories from Avenues

'''

import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv('demo_data_geo.csv')
df.columns = {'categories', 'avenues', 'scores'}
unique_avenues = df['avenues'].unique()
unique_categories = df['categories'].unique()
count = 0

# Creating a list where unique avenues are replaced with unique integer numbers
geo_dict = {}
for av in unique_avenues:
    for ind in df.index:
        if df['avenues'][ind] == av:
            geo_dict[count] = df['avenues'][ind]
            df['avenues'][ind] = count
    count += 1

# Creating a list where unique categories are replaced with another set of unique integer numbers

count = 120

category_dict = {}

for cat in unique_categories:
    for ind in df.index:
        if df['categories'][ind] == cat:
            category_dict[count] = df['categories'][ind]
            df['categories'][ind] = count
    count -= 1


dataset = zip(df.avenues.values, df.scores.values)
target = df.categories.values

dataset = np.asarray(dataset, dtype = int)
target = np.asarray(target, dtype = int)


# Calculating a predcitive model and measuring the accuracy

from sklearn.metrics import accuracy_score
from sklearn import tree

rfc = tree.DecisionTreeClassifier()

y_pred = rfc.fit(dataset, target).predict(dataset)

lst = []

for y in y_pred:
     lst.append(category_dict[y])
print lst

acc_score = accuracy_score(target, y_pred)
print "\n\nAccuracy Score for the Random Forest classifier on Categories is :", acc_score*100,"%"


'''

This code section is implemented for predicting Geo-avenues based on Categories and Scores

'''

print "Now predicting avenues from Categories based on Scores"
dataset = zip(df.categories.values, df.scores.values)
target = df.avenues.values


dataset = np.asarray(dataset, dtype = int)
target = np.asarray(target, dtype = int)

# Calculating a predcitive model and measuring the accuracy

from sklearn.metrics import accuracy_score
from sklearn import tree

rfc = tree.DecisionTreeClassifier()

y_pred = rfc.fit(dataset, target).predict(dataset)

lst = []

for y in y_pred:
     lst.append(geo_dict[y])

print lst

acc_score = accuracy_score(target, y_pred)
print "\n\nAccuracy Score for the Random Forest classifier on Avenues is :", acc_score*100,"%"
