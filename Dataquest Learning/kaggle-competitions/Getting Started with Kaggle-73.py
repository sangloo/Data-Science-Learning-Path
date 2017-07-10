## 2. Examining the Data With .describe() ##

# We can use the pandas library in Python to read in the CSV file
# This creates a pandas dataframe and assigns it to the titanic variable
titanic = pandas.read_csv("titanic_train.csv")

# Print the first five rows of the dataframe
print(titanic.head(5))
print(titanic.describe())

## 3. Cleaning Up Missing Data ##

# The titanic variable is available here
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

## 5. Converting the Sex Column to Numeric ##

# Find all of the unique genders 
# The column appears to contain the values male and female only
print(titanic["Sex"].unique())

# Replace all the occurences of male with the number 0
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

## 6. Converting the Embarked Column ##

# Find all of the unique values for "Embarked"
print(titanic["Embarked"].unique())
titanic["Embarked"] = titanic["Embarked"].fillna("S")

titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

## 10. Evaluating Prediction Error ##

import numpy as np

# The predictions are in three separate NumPy arrays  
# Concatenate them into a single array 
# We concatenate them on axis 0, because they only have one axis
predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes (the only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0
accuracy = sum(predictions[predictions == titanic["Survived"]]) / len(predictions)

## 12. Processing the Test Set to Replace Values ##

titanic_test = pandas.read_csv("titanic_test.csv")
titanic_test["Age"] = titanic_test["Age"].fillna(titanic["Age"].median())
titanic_test["Fare"] = titanic_test["Fare"].fillna(titanic_test["Fare"].median())
titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0 
titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1
titanic_test["Embarked"] = titanic_test["Embarked"].fillna("S")

titanic_test.loc[titanic_test["Embarked"] == "S", "Embarked"] = 0
titanic_test.loc[titanic_test["Embarked"] == "C", "Embarked"] = 1
titanic_test.loc[titanic_test["Embarked"] == "Q", "Embarked"] = 2