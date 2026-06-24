#TASK (2): Exploratory Data Analysis (EDA)........
#Before starting analysis, we define important questions:

# Q-1)Which category generates the highest sales?
# Q-2)Which region has the highest profit?
# Q-3)Does discount affect profit?
# Q-4)Which sub-category is most profitable?
# Q-4)Are there any loss-making products?
# Q-5)Which segment contributes most to revenue?

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("SampleSuperstore.csv")
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)
print(df.columns)
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
#........(1) Category distribution..........
print(df['Category'].value_counts())

sns.countplot(x='Category', data=df)
plt.show()
#.......(2)Segment analysis......
print(df['Segment'].value_counts())

sns.countplot(x='Segment', data=df)
plt.show()
#.......(3)Region analysis.....
print(df['Region'].value_counts())

sns.countplot(x='Region', data=df)
plt.show()
#Category vs Sales....
df.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.title("Category vs Sales")
plt.show()
#..........Category vs Profit....
df.groupby('Category')['Profit'].sum().plot(kind='bar')
plt.title("Category vs Profit")
plt.show()
#.........Region vs Sales.....
df.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title("Region vs Sales")
plt.show()
#......Discount vs Profit
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()
#.......Outlier check.....
sns.boxplot(x=df['Sales'])
plt.show()

sns.boxplot(x=df['Profit'])
plt.show()

#Correlation.........
sns.heatmap(df[['Sales','Quantity','Discount','Profit']].corr(), annot=True)
plt.show()
#.......Insights & Conclusions......

# Technology category generates highest sales.
# Some sub-categories generate negative profit.
# Higher discounts reduce profit.
# Sales contain extreme outliers.
# Profit has both very high gains and heavy losses.
# West region performs best in sales