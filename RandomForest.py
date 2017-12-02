'''
Implementing Random Forest Classifier on the Dataset for predicting Business categories from Avenues
'''

import pandas as pd
import numpy as np
from pandas import DataFrame,concat

df = pd.read_csv('demo_data_geo.csv')
row = df.columns
d = row.values
df.columns = {'categories', 'avenues', 'scores'}

line = DataFrame({"categories": "Entertainment", "avenues": "Ahwatukee", "scores": -0.62388}, index=[0])
df_2 = concat([df.ix[:0], line, df.ix[1:]]).reset_index(drop=True)
df = df_2
#print df

min = df['scores'].min()
print min,"\t",max
df['scores'] = df['scores'] + 6
print df
df.to_csv("dataset_1.csv")
unique_avenues = df['avenues'].unique()
unique_categories = df['categories'].unique()
df_lst = df.values

count = 0

# Creating a list where unique avenues are replaced with unique integer numbers

geo_dict = {}

for av in unique_avenues:
    for ind in df.index:
        if df['avenues'][ind] == av:
            geo_dict[count] = df['avenues'][ind]
            df['avenues'][ind] = count
    count += 1
print "printing df"
print df


# Creating a list where unique categories are replaced with another set of unique integer numbers

count = 120

category_dict = {}

for cat in unique_categories:
    for ind in df.index:
        if df['categories'][ind] == cat:
            category_dict[count] = df['categories'][ind]
            df['categories'][ind] = count
    count -= 1
print df

dataset = zip(df.avenues.values, df.scores.values)
print "Printing dagtaset", dataset
target = df.categories.values
dataset = np.asarray(dataset, dtype = int)
target = np.asarray(target, dtype = int)

# Calculating a predcitive model and measuring the accuracy

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
y_pred = rfc.fit(dataset, target).predict(dataset)
lst = []
for y in y_pred:
     lst.append(category_dict[y])

zipped_data = list(zip(df_lst, lst))
print "\nPrinting zipped data:"
print zipped_data

acc_score = accuracy_score(target, y_pred)
print "Accuracy Score for the Random Forest classifier is :", acc_score


'''
This code is for predicting avenues based on Categories and Scores
'''

print "\n\nNow predicting avenues from Categories based on Scores\n"
dataset = zip(df.categories.values, df.scores.values)
target = df.avenues.values

dataset = np.asarray(dataset, dtype = int)
target = np.asarray(target, dtype = int)

# Calculating a predcitive model and measuring the accuracy

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
y_pred = rfc.fit(dataset, target).predict(dataset)
lst = []

for y in y_pred:
     lst.append(geo_dict[y])


acc_score = accuracy_score(target, y_pred)
print "\n\nAccuracy Score for the Random Forest classifier on Avenues is :", acc_score*100,"%"
