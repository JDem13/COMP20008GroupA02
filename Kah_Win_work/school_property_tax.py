import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')


# Reading csvs
loc_df = pd.read_csv("School_Location_2020.csv")
tax_df = pd.read_csv("Land_Tax_2018.csv")

# top 20 and bottom 20 locations of number of schools
print(loc_df['LGA_Name'].value_counts().head(20))
print(loc_df['LGA_Name'].value_counts().tail(20))


# top 20 and bottom 20locations of land tax
tax_sorted = tax_df.sort_values('Total proportionate tax', ascending=False)
print(tax_sorted[['Municipality', 'Total proportionate tax']].drop(tax_sorted.index[[0,1]]).head(20))
print(tax_sorted[['Municipality', 'Total proportionate tax']].tail(20))


