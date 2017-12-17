# Market-Research-Analysis

## Introduction
We built a data model to predict the type of business/products that would thrive at a
given Geo-Location by analyzing the data retrieved from crowd-sourced platforms like Yelp.
Yelp API was used to retrieve information categorically based on the given business product Id
pertaining to different Geographic Coordinates in and around Phoenix, Arizona, US. The data
was segregated based on Geo avenues and on product types separately. Further, Data
Visualization techniques were used to present a visual communication of the data and Machine
Learning algorithms were implemented to help in prediction and in checking the accuracy of the
model built.

## Requirements  

Works on Python 2 as of now.

'pip install python'

pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

'pip install pandas'

matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

'sudo pip install python-matplotlib'

Scikit-learn is a free software machine learning library for the Python programming language
'pip install -U scikit-learn'


## Data Normalization
Data Normalization is a method used to standardize the range of independent variables or features of data. It is generally performed during the data preprocessing step.

f_norm = (f - f_mean) / (f_max - f_min)
