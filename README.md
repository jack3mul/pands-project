# pands-project
investigation into Fisher's Iris Data Set

I found the data set online at the location: https://archive.ics.uci.edu/ml/datasets/iris

I verified the data had the reported number of lines in it and had data for three species as reported.
This was done by using commands
1. print(data.info())   -> confirms the layout
2. data.isnull().sum()  -> checks for incomplete data (zeros)

The data was analysed using histograms and scatter plots; these were then used for the author's 
analysis.

The colour scheme chosen for these plots is:
        red:    Iris-setosa
        blue:   Iris-virginica
        green:  Iris-versicolor
(map function used to associate the above)


Sepal Length and Sepal width
[ ref - Sepal Characteristics.png -- scatter plot created using the data of Sepal Length and Sepal Width]

This scatter plot show the Iris-setosa has the lowest sepal length and the highest sepal width. The data for Iris-setosa appears to me to be densely located in this plot and is removed from the other data which I believe would make it easier to identify this by dimensions alone.

The data for the Iris-virginica and the Iris-versicolor has more data overlapping and it would be more difficult to identify one of these flowers. There is one attribute which would identify a flower; should it have a sepal length of greater than 7 it appears from this data that this flower would be a Iris-virginica because this flower is the only one listed which is in this range of sepal lengths.


Petal Length and Petal width
[ ref - Petal Characteristics.png -- scatter plot created using the data of Petal Length and Petal Width]

The Petal width and length values of the Iris-setosa are lowest in this dataset and it may be possible to identify a plane with these smaller characteristics because they are densely pooled together and separate to the rest of the data.

The Iris-virginica has larger petal lengths and widths but its data overlaps with the Iris-versicolor which would make identifying to good degree of probability as being hard. The Iris-versicolor would be hardest to identify because its ranges in this dataset span the data of the Iris-virginica without having any values in the upper limits. There is a range of the data where there is no Iris-versicolor so it may be possible to exclude a flower as being a versicolor in this range: petal width  approx 1.5cm to ~2cm 