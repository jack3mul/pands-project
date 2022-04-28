from nbformat import write
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris_data.csv")

# all modules imported and data set loaded into using pandas

#open file to write output to
with open ("analysis.txt","w") as f:
    #f.write(str(data.head()))      #NB remember:- cast to string !!
    #(data.keys())                 # checking the keys - had earlier issue with space in front of key name
    
    #Write following to output file specified.
    #Cast to string where needed

    f.write("************** IRIS DATA SET ANALYSIS **************\n\n")
    f.write("\n***********\n")
    f.write("Check the integrity of the Data.")
    f.write("Details of the data are:\n ")
    f.write(str(data.info()))
    f.write("\nCheck for null values: \n")
    f.write(str(data.isnull().sum()))
    f.write("\n***********\n")
    f.write("\nNo null values found in the data set\n")
    f.write("\n***********\n")
    f.write("Confirm that there are equal value for all attributes:\n")
    f.write(str(data.value_counts(" species")))
    "\n***********\n"
    f.write(str(data.shape))
    f.write("\n***********\n")
    f.write(str(data.describe()))
    f.write("\n***********\n")
    f.write("\nThe correlation of the data is seen in this table:\n")
    f.write(str(data.corr()))
    f.write("\n***********\n")

    f.write("\nMy analysis of the data is as follows:\n\n")
    with open("README.md","r") as input:
        f.write(str(input.read())) 
    f.write("\n\n\n**********END**********")

features = ['sepal_length', ' sepal_width', ' petal_length', ' petal_width']
#this will cut down on retyping these long names..now ref features[0]..[3]

#loop to automate histogram creation - repetitive so should be automated
#close aech plt before moving on - had encountered errors here previously
for feature in features:
    plt.hist([data[feature]])
    plt.title(feature)
    plt.xlabel(feature)
    plt.ylabel("number")
    #plt.show()                 Required for testing only
    plt.savefig(feature)
    plt.close()                 #Clean - without this was getting issues and incorrect plots

plt.hist([data[features[0]], data[features[1]], data[features[2]], data[features[3]]], label=[features[0], features[1], features[2], features[3]])
plt.legend()
plt.savefig("combined_hist")  # this will have all plotted together
plt.close()

#Scatter plots



colors = {'Iris-setosa':'red', 'Iris-virginica':'blue','Iris-versicolor':'green'}
#set preferences in here for different elements and colours - personal choice - 

plt.scatter(data[features[0]],data[features[1]],c=data[' species'].map(colors))
# map the colour back to the species
plt.xlabel(features[0])
plt.ylabel(features[1])
plt.title('Sepal Characteristics')
#plt.show()
plt.savefig('Sepal Characteristics')
plt.close()

#considered automating this and plugging the next values back in i=0, i++ and then i=2.
#only runs twice..went manual in the end

plt.scatter(data[features[2]],data[features[3]],c=data[' species'].map(colors))
plt.xlabel(features[2])
plt.ylabel(features[3])
plt.title('Petal Characteristics')
#plt.show()
plt.savefig('Petal Characteristics')
plt.close()

exit(0)
