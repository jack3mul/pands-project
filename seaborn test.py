import seaborn as sns
import pandas as pd

data = pd.read_csv("iris_data.csv")
sns.pairplot(data, hue = " species", height = 1)