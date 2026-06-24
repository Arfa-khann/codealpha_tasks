import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("ecommerce_sales_analytics_5000.csv", parse_dates=["order_date"])
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)
print(df.columns)
#revenue sum.......
print(df["revenue"].sum())
print(df.groupby("region")["revenue"].sum())

sns.barplot(data=df, x="region", y="revenue")
plt.show()
#.....payment method....
df["payment_type"]=df["payment_method"].map({
    "Card": "Digital",
    "wallet":"Digital",
    "COD": "Cash"
}).fillna("Other")
print(df["payment_type"].unique())

print(df[["payment_type","payment_method"]].head())

print(df.groupby("payment_type").size())

def renvenue_category(row):
    if row ["revenue"] > 500:
        return "high"
    elif row["revenue"] >= 200:
        return "medium"
    else:
        return "low"
df["renvenue_category"]=df.apply(renvenue_category, axis=1)
print(df["renvenue_category"].value_counts())

print(df[["revenue","renvenue_category"]].sample(10))

def add_profil(data):
    data["profit"]=data["revenue"] * 0.2
    return data
def add_net_revenue(data):
    data["net_revenue"]= data["revenue"] -data["profit"]
    return data
df=(df.pipe(add_profil).pipe(add_net_revenue))
print(df[["revenue", "profit", "net_revenue"]].head(10))
cols = ["revenue", "profit", "net_revenue"]
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")
plt.title("Revenue, Profit & Net Revenue Correlation")
plt.show()
df.groupby("order_date")["revenue"].sum().plot()
plt.title("Revenue Over Time")
plt.show()

df["payment_method"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.show()
# Insights........
# 1. Which region has highest revenue?
# 2. Which category performs best?
# 3. Does discount impact revenue?
# 4. Which payment type is most used?



