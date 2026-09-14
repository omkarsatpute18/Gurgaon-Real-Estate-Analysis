import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
# print(df.head())

# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.columns.tolist())


df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
# print(df.columns)

df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(float)

# print(df["area"])
# print(df["price"])
# print(df["rate_per_sqft"])


# print(df.columns.tolist())

df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()

# print(df["status"])
# print(df["flat_type"])
# print(df["rera_approval"])


df = df.drop_duplicates()


# print(df.head())

#Question 1: Which is the costliest flat?
costliest = df.loc[df["price"].idxmax()]
# print(costliest)

#Question 2: Which locality has the highest average price?
highest_average_price = df.groupby("locality")["price"].mean().sort_values(ascending=False)
# print(highest_average_price)

#Question 3: Which locality has the highest rate per square foot?
highest_rate_per_sqft = df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)
# print(highest_rate_per_sqft)

#Question 4: Ready-to-move vs Under-construction pricing
Q4 = df.groupby("status")["price"].median()
# print(Q4)

#Question 5: Does RERA approval affect pricing?

Q5 = df.groupby("rera_approval")["price"].median()
# print(Q5)

#Question 6: How does area impact price?
sns.scatterplot(x="area",y="price",data=df)
# plt.show()

# Question 7: Which BHK configuration is most expensive?

Q7 = df.groupby("bhk_count")["price"].mean()
# print(Q7)

# Question 8: Which property type is the costliest?
Q8 = df.groupby("property_type")["price"].max()
# print(df.columns.tolist())
# print(Q8)

# Question 9: Do certain builders price higher?

Q9 = df.groupby("company_name")["price"].mean().sort_values(ascending=False)
# print(Q9)

# Question 10: Are larger homes more expensive per sqft?

sns.scatterplot(x="area",y="rate_per_sqft",data=df)
plt.show()


#finalllllyyyy...........Conclude with the project..
#Happy Ending.....
