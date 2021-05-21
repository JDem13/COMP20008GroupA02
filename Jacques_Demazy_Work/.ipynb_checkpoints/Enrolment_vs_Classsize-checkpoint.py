import pandas as pd
import csv
import matplotlib.pyplot as plt


#class size records from 2007 to 2019
classsize2007_2019 = pd.read_csv("classsize.csv")
classsize2007_2019 = classsize2007_2019.iloc[1:,7:]

#all fte high school enrolments from 2007 to 2019

ern_2007 = pd.read_csv("2007enrolments.csv")
ern_2008 = pd.read_csv("2008enrolments.csv")
ern_2009 = pd.read_csv("2009enr.csv") 
ern_2010 = pd.read_csv("2010enr.csv")
ern_2011 = pd.read_csv("2011enrolments.csv")
ern_2012 = pd.read_csv("2012enrolments.csv")
ern_2013 = pd.read_csv("2013enrolments.csv")
ern_2014 = pd.read_csv("2014enrolments.csv")
ern_2015 = pd.read_csv("2015enr.csv")
ern_2016 = pd.read_csv("2016enrolments.csv")
ern_2017 = pd.read_csv("2017enrolments.csv")
ern_2018 = pd.read_csv("2018enrolments.csv")
ern_2019 = pd.read_csv("2019enrolments.csv")

#extracting total enrolments for state
ern_2007 = ern_2007.loc[:,'Grand Total'].sum()
ern_2008 = ern_2008.loc[:,'Grand Total'].sum()
ern_2009 = ern_2009.loc[:,'Grand Total'].sum()
ern_2010 = ern_2010.loc[:,'Grand Total'].sum()
ern_2011 = ern_2011.loc[:,'Grand Total'].sum()
ern_2012 = ern_2012.loc[:,'Grand Total'].sum()
ern_2013 = ern_2013.loc[:,'Grand Total'].sum()
ern_2014 = ern_2014.loc[:,'Grand Total'].sum()
ern_2015 = ern_2015.loc[:,'Grand Total""'].sum()
ern_2016 = ern_2016.loc[:,'Grand Total'].sum()
ern_2017 = ern_2017.loc[:,'Grand Total'].sum()
ern_2018 = ern_2018.loc[:,'Grand Total""'].sum()
ern_2019 = ern_2019.loc[:,'Grand Total""'].sum()


#create series with tot enrolments from 2007 to 2019
tot_enrolments = {'2007': ern_2007, '2008': ern_2008, '2009': ern_2009, '2010': ern_2010, '2011': ern_2011, 
                 '2012': ern_2012, '2013': ern_2013, '2014': ern_2014, '2015': ern_2015, '2016': ern_2016,
                  '2017': ern_2017, '2018': ern_2018, '2019': ern_2019,}
tot_enrolments = pd.Series(tot_enrolments)

#plot enrolments with classsizes
plt.scatter(tot_enrolments, classsize2007_2019)
plt.savefig("enrolments_vs_classzie.png")


#normalise both sets of data
classsize2007_2019 = classsize2007_2019 / classsize2007_2019.max().max()
tot_enrolments = tot_enrolments / tot_enrolments.max()


#create new normalised plots
plt.scatter(tot_enrolments, classsize2007_2019)
plt.xlim(0.825,1)
plt.ylim(0.97,1.001)
plt.savefig("enrolments_vs_classzie_normalized.png")

 
#compute Pearson Correlation betweem two sets of data

#compute sample means 
classsize2007_2019 = classsize2007_2019.squeeze()

x_bar = 0
for i in classsize2007_2019:
    x_bar += i
x_bar = x_bar / classsize2007_2019.size

y_bar = 0
for i in tot_enrolments:
    y_bar += i
y_bar = y_bar / tot_enrolments.size

pearson_correlation = 0
x_var = 0
y_var = 0

for i in (0,tot_enrolments.size-1):
    pearson_correlation += ((classsize2007_2019[i]-x_bar)* (tot_enrolments[i]-y_bar))
    x_var += (classsize2007_2019[i]-x_bar)**2
    y_var += (tot_enrolments[i]-y_bar)**2

pearson_correlation = pearson_correlation / (x_var*y_var)**0.5

print(pearson_correlation)
    

    