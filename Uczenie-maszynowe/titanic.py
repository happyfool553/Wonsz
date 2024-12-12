#pip3 install pandas
#pip3install scikit-learn
#pip3 install matplotlib --to sie w terminalu pisze

import pandas as pd #stworzenie krotszej nazwy do odwolan
from sklearn import preprocessing
from sklearn import tree
from sklearn import model_selection
from sklearn import ensemble
from sklearn.tree import plot_tree     #pobieranie szczegolnych funkcji z dodatkow
import matplotlib.pyplot as plt
import matplotlib.image as img
from sklearn import neighbors

data = pd.read_csv("train.csv", sep = ",")
print(data.head(30))
print(data.dtypes)

print(data.describe())
print(data.isnull().sum())

labelEncoder = preprocessing.LabelEncoder()
labelEncoder.fit(data['Sex'])
data['Sex'] = labelEncoder.transform(data['Sex'])

y = data['Survived']