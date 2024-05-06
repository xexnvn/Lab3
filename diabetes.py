#
# Eva
# Pandas Practice
# 

import pandas as pd

# Load data
df = pd.read_csv("/Users/mooon/Desktop/mon_python/diabetes.csv")

# Inspect structure
df.shape
# df.info()

# Inspect value
df.head()
df.tail()

# Add missing values
df2 = df.copy()
df2.loc[2:5, "Pregnancies"] = None
df2.head(10)

# Add missing values
df2.isnull().sum()
df2.shape

# Remove rows with missing value
df3 = df2.copy()
df3 = df3.dropna()
print(df3.shape)

# Create a new column
df2['Glucose_Insulin_Ratio'] = df2['Glucose'] / df2['Insulin']
print(df2.head())