#
# Eva
# Pandas Practice
# 

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("/Users/mooon/Desktop/mon_python/smoker.csv")

# Inspect structure
df.shape
df.info()

# Inspect value
df.head()
df.tail()

# Visualize
df["smoker"].hist()
plt.show()

# Count rows of same value
df["smoker"].value_counts()
df["treatment"].value_counts()
df["outcome"].value_counts()

# Mean
df["smoker"].mean()
df["treatment"].mean()
df["outcome"].mean()

# Sum
df.sum()
df.sum(axis = 1)