import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("iris_data.csv")

# all modules imported and data set loaded into using pandas

#open file to write output to
#open ("analysis.txt") as f:

print(data.head())
print(data.keys())   # checking the keys - had earlier issue with space in front of key name
print(data.loc[::50])

print("Details of the data are:\n ")
print(data.info())
print(f"Check for null values: \n{data.isnull().sum()}")
print(data.shape)
print(data.describe())
print(data.corr())

print("My analysis of the data is as follows:")

features = ['sepal_length', ' sepal_width', ' petal_length', ' petal_width']


for feature in features:
    plt.hist([data[feature]])
    plt.title(feature)
    plt.legend()
    plt.xlabel(feature)
    plt.ylabel("number")
    #plt.show()
    plt.savefig(feature)

plt.hist([data[features[0]], data[features[1]], data[features[2]], data[features[3]]], label=[features[0], features[1], features[2], features[3]])
plt.legend()
plt.savefig("combined_hist")

#Scatter plots



colors = {'Iris-setosa':'red', 'Iris-virginica':'blue','Iris-versicolor':'green'}

plt.scatter(data[features[0]],data[features[1]],c=data[' species'].map(colors))
plt.xlabel(features[0])
plt.ylabel(features[1])
plt.title('Sepal Characteristics')
#plt.show()
plt.savefig('Sepal Characteristics')

plt.scatter(data[features[2]],data[features[3]],c=data[' species'].map(colors))
plt.xlabel(features[2])
plt.ylabel(features[3])
plt.title('Petal Characteristics')
#plt.show()
plt.savefig('Petal Characteristics')


