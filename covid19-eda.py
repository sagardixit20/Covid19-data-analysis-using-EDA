#EDA ON covid19 (indian) DATASET
#IMPORTING THE REQUIRED LIBRARIES FROM PYTHON
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

covid = pd.read_csv(r"C:\Users\ASUS\Documents\datasets for visulaization\Latest Covid-19 India Status (1).csv")
#print(covid.head())
#print(covid.shape)

#get the information of discharged people
dis = covid['Discharged'].value_counts()
#print(dis)
#first 5 discharged people
dis = covid['Discharged'].value_counts()[0:5]
#print(dis)

#making barplot for states and discharged people
plt.figure(figsize=(8,10))
sns.barplot(data=covid, y = "State/UTs", x="Total Cases")
#print(plt.show())

#scatter plot
sns.scatterplot(y="Deaths",x="State/UTs",data=covid)
#print(plt.show())

#pairplot
sns.pairplot(covid)
#print(plt.show())


df2 = covid.sort_values(by='Death Ratio', ascending=False).head()
states = df2['State/UTs']
ratio = df2['Death Ratio']
plt.barh(states, ratio)
plt.xlabel('Death Ratio (%)')
plt.ylabel('State')
plt.title('State with more death ratio in India')
#plt.show()

#making a pie-chart
plt.figure(figsize=(6,6))
plt.pie(list(covid['Discharged'].value_counts()[0:5]),labels=list(covid['State/UTs'].value_counts()[0:5].keys()),autopct='%0.1f%%')
#print(plt.show())

sns.heatmap(covid.isnull())
#print(plt.show())
sns.relplot(x = 'Total Cases', y ='Discharged', hue = 'State/UTs', data = covid)
plt.show()