## 3. Introduction to the Data Set ##

import pandas as pd

titanic = pd.read_csv('train.csv')
titanic = titanic[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].dropna()

## 4. Creating Histograms In Seaborn ##

import seaborn as sns
sns.distplot(titanic["Age"])
plt.show()

## 5. Generating A Kernel Density Plot ##

sns.kdeplot(titanic["Age"], shade = True)
plt.xlabel("Age")
plt.show()

## 6. Modifying The Appearance Of The Plots ##

sns.kdeplot(titanic["Age"], shade = True)
sns.set_style("white")
sns.despine( left = True, bottom = True)
plt.xlabel("Age")

## 7. Conditional Distributions Using A Single Condition ##

g = sns.FacetGrid(titanic, col="Pclass", size = 6)
g.map(sns.kdeplot, "Age", shade = True)

sns.despine(bottom = True, left = True)
plt.show()

## 9. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 10. Adding A Legend ##

g = sns.FacetGrid(titanic, col = "Survived", row = "Pclass", hue = "Sex", size = 3)
g.map(sns.kdeplot, "Age", shade = True).add_legend()
sns.despine(top = True, bottom = True, left = True, right = True)

plt.show()