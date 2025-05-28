import pandas as pd

#   CLEANING THE DATA

# df = pd.read_csv("data.csv")

# print(df.head())
# print(df.info())

# print(df.isnull().sum()) # shows how many nulls in each column

# print(df.dtypes) # lets us see data types in each column

# text_columns = df.select_dtypes("object").columns
# number_columns = df.select_dtypes(include=["int64", "float64"]).columns  # seperating different datatype columns

# print(df.isnull().sum()[df.isnull().sum() > 0]) # this code shows only the columns with null

# df.drop(columns="Cabin", inplace=True) # removing the column 'Cabin' because there a lot of empty spaces

# df["Embarked"].fillna(value=(df["Embarked"].mode()[0]), inplace=True)  #  filling the column 'Embarked' with the most common value in the column
# df["Age"].fillna(value=df["Age"].mean(), inplace=True)  #  filling the column 'Age' with the average value in the column

# df.to_csv("cleaned_data.csv", index=False) # saving the cleaned data

#_______________________________________________________________________________________

# ANALYZING DATA

# print(df["Survived"].value_counts())  #Shows how many people survived

# print(df["Pclass"].value_counts())  #shows how many people in each class

# print(df["Age"].agg(["mean", "max", "min"]))   #shows average, minimum, maximum ages

# print(df.value_counts("Sex"))  #Counts how many men and women was in titanic

# print(df.groupby("Sex")["Survived"].sum())  #shows how many men and women survived

#_______________________________________________________________________________________

#  VISUALIZATION

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_data.csv")

# sns.countplot(x="Survived", data=df)
# plt.show()  #Shows Survived and died number of people

# sns.countplot(data=df, x="Pclass", hue="Survived", )
# plt.title("Survival in each class")
# plt.xlabel("Class")
# plt.ylabel("Count")
# plt.show()   #Shows how many people died and survived in each class

# sns.boxplot(x="Survived", y="Age", data=df)
# plt.show()   # shows relationship between age and survival rate

# sns.histplot(df['Fare'], bins=30, kde=True)
# plt.title("Fare Distribution")
# plt.xlabel("Fare")
# plt.ylabel("Count")
# plt.show()   # shows Fare distribution

# sns.scatterplot(x='Age', y='Fare',hue="Survived", data=df)
# plt.title("Relationship between Age and Fare")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()  #Shows relationship between age, fare, and survival

# print(df.groupby("Sex")["Fare"].sum())  # Compares sum of fare of male and female
# sns.boxplot(x="Sex", y="Fare", data=df)
# plt.title("Male vs Female")
# plt.show()  # Shows the comparison

# sns.countplot(x="Embarked", hue="Survived", data=df)
# plt.title("Survival by Embarked Port")
# plt.xlabel("Embarked Port")
# plt.ylabel("Count")
# plt.show()  # Shows how many people died and survived in each class
