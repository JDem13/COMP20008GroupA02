import pandas as pd

#read files containing Property Tax by municipality info and
#post school destinations for students in Victoria in 2019

property_tax = pd.read_csv("PropertyTax2019.csv")
post_school = pd.read_csv("2019PostSchool.csv")



# extract data to be used in comparison
property_tax = property_tax.sort_values(by = 'Percentage of total tax (%)', ascending = False)
print(property_tax['Total proportionate tax'])