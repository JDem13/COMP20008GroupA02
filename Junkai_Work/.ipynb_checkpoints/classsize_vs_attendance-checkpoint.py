
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('dv292-govschoolsclasssizesecondary2001-2019.csv',encoding = 'ISO-8859-1')
df10 = pd.read_csv('dv18-2010studentattendancerates.csv',encoding = 'ISO-8859-1')
df11 = pd.read_csv('dv19-2011studentattendancerates.csv',encoding = 'ISO-8859-1')
df12 = pd.read_csv('38-dv2012attendancerates.csv',encoding = 'ISO-8859-1')
df14 = pd.read_csv('dv174-govschstudentattendrates2014.csv',encoding = 'ISO-8859-1')
df15 = pd.read_csv('dv213-govstudentatttendancerates2015.csv',encoding = 'ISO-8859-1')
df16 = pd.read_csv('dv262-govschoolsstudentattendancerates16.csv',encoding = 'ISO-8859-1')
df17 = pd.read_csv('dv263-govschoolsstudentattendancerates2017.csv',encoding = 'ISO-8859-1')
df18 = pd.read_csv('dv278-govstudentatttendancerates2018.csv',encoding = 'ISO-8859-1')

secondary = {'2010':df['2010'][0],'2011':df['2011'][0], '2012':df['2012'][0], '2014':df['2014'][0], '2015':df['2015'][0], '2016':df['2016'][0], '2017':df['2017'][0], '2018':df['2018'][0]}
primary = {'2010':df['2010'][1],'2011':df['2011'][1], '2012':df['2012'][1], '2014':df['2014'][1], '2015':df['2015'][1], '2016':df['2016'][1], '2017':df['2017'][1], '2018':df['2018'][1]}

# in dataset for 2016-2018, the form of data have '%' in the end we need to strip them
data16s = df16['Ungraded secondary'][5].strip("%")
data17s = df17['Ungraded secondary'][5].strip("%")
data18s = df18['Ungraded secondary'][5].strip("%")

data16p = df16['Ungraded primary'][5].strip("%")
data17p = df17['Ungraded primary'][5].strip("%")
data18p = df18['Ungraded primary'][5].strip("%")

atdcesec = {'2010':int(df10['Secondary ungraded'][5]), '2011':int(df11['Secondary ungraded'][5]), '2012':int(df12['Secondary ungraded'][5]), '2014':int(df14['Secondary ungraded'][5]), '2015':int(df15['Secondary ungraded'][5]), '2016':int(data16s), '2017':int(data17s), '2018':int(data18s)}

atdcepri = {'2010':int(df10['Primary ungraded'][5]), '2011':int(df11['Primary ungraded'][5]), '2012':int(df12['Primary ungraded'][5]), '2014':int(df14['Primary ungraded'][5]), '2015':int(df15['Primary ungraded'][5]), '2016':int(data16p), '2017':int(data17p), '2018':int(data18p)}


ssecodary = pd.Series(secondary)
sprimary = pd.Series(primary)
satdcesec = pd.Series(atdcesec)
satdcepri = pd.Series(atdcepri)

df1 = pd.DataFrame({'Secondary':ssecodary, 'Primary':sprimary})
df2 = pd.DataFrame({'Secondary ungraded attendence':satdcesec, 'Primary ungraded attendence':satdcepri})

#normalise data
df1['Secondary'] = df1['Secondary'] / df1['Secondary'].max()
df2['Secondary ungraded attendence'] = df2['Secondary ungraded attendence'] / df2['Secondary ungraded attendence'].max()

#secondary school attendance vs classsize
plt.scatter(df1['Secondary'], df2['Secondary ungraded attendence'])
plt.ylabel('Average Attendance')
plt.xlabel('Average Class size')
plt.savefig("classsize_vs_attendance.png")

df1.plot()
plt.ylabel("Average classsize")
plt.xlabel("Year")
plt.grid(True)
plt.title("Average classsize change in years")
plt.ylim(15,25)
plt.legend()

plt.savefig("classsize.png")
plt.show()


df2.plot()
plt.ylabel("Average class attendence in percentege")
plt.xlabel("Year")
plt.grid(True)
plt.title("Average class attendence in years")
plt.ylim(83,93)
plt.legend()

plt.savefig("attendence.png")
plt.show()


#compute sample means correlation

x_bar = 0
for i in satdcesec:
    x_bar += i
x_bar = x_bar / satdcesec.size

y_bar = 0
for i in ssecodary:
    y_bar += i
y_bar = y_bar / ssecodary.size

pearson_correlation = 0
x_var = 0
y_var = 0

for i in (0,ssecodary.size-1):
    pearson_correlation += ((satdcesec[i]-x_bar)* (ssecodary[i]-y_bar))
    x_var += (satdcesec[i]-x_bar)**2
    y_var += (ssecodary[i]-y_bar)**2

pearson_correlation = pearson_correlation / (x_var*y_var)**0.5

print(pearson_correlation)
