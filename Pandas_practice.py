#
# Eva
# Pandas Practice
# 

import pandas as pd

# Load data
df = pd.read_csv("/Users/mooon/Desktop/mon_python/smoker.csv")

# Inspect structure
df.shape
df.info()

df.head()
df.tail()