# Titanic Data Analysis Project

This project is part of my data analyst portfolio, focused on analyzing the Titanic dataset using Python and pandas. It includes essential data cleaning, exploratory data analysis (EDA), and visualizations to understand survival patterns and demographic insights from the dataset.

## 📁 Dataset

The dataset contains information about the passengers on the Titanic, such as:

* Age
* Sex
* Passenger class (Pclass)
* Number of siblings/spouses aboard (SibSp)
* Number of parents/children aboard (Parch)
* Fare
* Embarked (port of embarkation)
* Survival status (Survived)

## 🧹 Data Cleaning

We handled missing values with the following steps:

* Filled missing `Embarked` values with the most common port.
* Replaced missing `Age` values with the mean age.
* Dropped the `Cabin` column due to excessive missing data.
* Saved the cleaned dataset as `cleaned_data.csv`.

## 📊 Exploratory Data Analysis

We answered several key questions:

### 1. Survival Count

```python
sns.countplot(x="Survived", data=df)
```

Shows how many passengers survived vs. died.

### 2. Survival by Class

```python
sns.countplot(x="Pclass", hue="Survived", data=df)
```

Helps us understand which class had higher survival rates.

### 3. Survival by Age

```python
sns.boxplot(x="Survived", y="Age", data=df)
```

Analyzes age distribution of survivors vs. non-survivors.

### 4. Fare by Gender

```python
sns.boxplot(x="Sex", y="Fare", data=df)
```

Shows how much fare men and women paid on average.

### 5. Survival by Embarkation Port

```python
sns.countplot(x="Embarked", hue="Survived", data=df)
```

Reveals survival distribution by port.

## ✅ Tools Used

* Python 🐍
* pandas 📊
* matplotlib & seaborn 📈

## 📌 Conclusion

This project helped me understand basic data analysis techniques using Python. We gained insights into which groups had higher survival chances based on class, age, sex, and port of embarkation.

## 💼 Author

\Bunyod
Aspiring Data Analyst
Tashkent, Uzbekistan

---

Feel free to clone or fork this repository if you're learning data analysis!
