# SeismoGuard
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Showing the first few rows of the dataset to understand its structure and contents.
df = pd.read_csv('D:/Capstone/STEAD Dataset/merge.csv/merge.csv')
# print(df.head())

# df.info()

# eq_df = df[df['trace_category'] == 'earthquake_local'].sample(5000, random_state=42)
# noise_df = df[df['trace_category'] == 'noise'].sample(5000, random_state=42)

# eq_df
# noise_df

# print("Missing values in earthquake_df:")
# print(eq_df.isnull().sum())

# print("\nMissing values in noise_df:")
# print(noise_df.isnull().sum())
