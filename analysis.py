import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("iris_data.csv")

# all modules imported and data set loaded into using pandas

print(data.head())
print(data.keys())   # checking the keys - had earlier issue with space in front of key name
print(data.loc[::50])

print("Details of the data are: ")
print(data.shape)
print(data.describe())
print(data.corr())
features = ['sepal_length', ' sepal_width', ' petal_length', ' petal_width']

#plt.hist([data[' petal_width']])
#plt.show()

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
plt.show()
