# 🏠 Real Estate Data Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a real estate dataset to understand property pricing patterns, locality-wise trends, property characteristics, and factors that influence the price of flats.

The analysis is performed using **Python**, with **Pandas** for data manipulation and **Matplotlib & Seaborn** for data visualization.

The main objective is to extract meaningful insights from the dataset and understand how factors such as **area, BHK configuration, locality, property type, RERA approval, construction status, and builder** affect property prices.

---

## 🎯 Objectives

The project aims to answer the following questions:

1. Which is the costliest flat in the dataset?
2. Which locality has the highest average property price?
3. Which locality has the highest average rate per square foot?
4. How do prices differ between ready-to-move and under-construction properties?
5. Does RERA approval affect property pricing?
6. How does property area impact price?
7. Which BHK configuration is the most expensive?
8. Which property type is the costliest?
9. Do certain builders price their properties higher?
10. Are larger homes more expensive per square foot?

---

## 🛠️ Technologies Used

* **Python** – Programming language
* **Pandas** – Data cleaning, manipulation, and analysis
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **CSV** – Dataset format
* **Jupyter Notebook / VS Code** – Development environment

---

## 📂 Project Structure

```text
Real-Estate-Data-Analysis/
│
├── data.csv
├── analysis.py
└── README.md
```

---

## 🔄 Data Preprocessing

Before performing the analysis, the dataset is cleaned and prepared using the following steps:

### 1. Loading the Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_csv("data.csv")
```

### 2. Cleaning Column Names

Column names are standardized by:

* Removing extra spaces
* Converting names to lowercase
* Replacing spaces with underscores

```python
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
```

### 3. Converting Numeric Columns

Price, area, and rate per square foot are converted into appropriate numeric formats after removing commas.

```python
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(float)
```

### 4. Standardizing Categorical Data

Categorical columns such as property status, RERA approval, and flat type are cleaned by removing unnecessary spaces and converting values to lowercase.

```python
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()
```

### 5. Removing Duplicate Records

Duplicate rows are removed to improve the reliability of the analysis.

```python
df = df.drop_duplicates()
```

---

## 📊 Analysis Performed

### 1. Costliest Flat

The property with the maximum price is identified using:

```python
costliest = df.loc[df["price"].idxmax()]
```

This helps identify the highest-priced property in the dataset.

---

### 2. Locality with Highest Average Price

Properties are grouped by locality and their average prices are calculated:

```python
highest_average_price = df.groupby("locality")["price"].mean().sort_values(ascending=False)
```

This identifies the localities where properties are generally more expensive.

---

### 3. Highest Rate per Square Foot

The average rate per square foot is calculated for each locality:

```python
highest_rate_per_sqft = df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)
```

This provides an understanding of property value based on area rather than total price.

---

### 4. Ready-to-Move vs Under-Construction Properties

Median property prices are compared based on construction status:

```python
Q4 = df.groupby("status")["price"].median()
```

Using the median helps reduce the influence of extremely expensive properties.

---

### 5. Impact of RERA Approval

Property prices are grouped according to RERA approval status:

```python
Q5 = df.groupby("rera_approval")["price"].median()
```

This helps investigate whether RERA-approved properties have different pricing patterns.

---

### 6. Relationship Between Area and Price

A scatter plot is used to visualize the relationship between property area and price:

```python
sns.scatterplot(x="area", y="price", data=df)
```

This helps determine whether larger properties generally have higher prices.

---

### 7. Most Expensive BHK Configuration

Average property prices are calculated for different BHK configurations:

```python
Q7 = df.groupby("bhk_count")["price"].mean()
```

This helps identify which BHK configuration has the highest average price.

---

### 8. Costliest Property Type

The maximum price for each property type is calculated:

```python
Q8 = df.groupby("property_type")["price"].max()
```

This allows comparison between different types of properties.

---

### 9. Builder-wise Pricing

Average property prices are calculated for each builder:

```python
Q9 = df.groupby("company_name")["price"].mean().sort_values(ascending=False)
```

This helps identify builders whose properties have higher average prices.

---

### 10. Area vs Rate per Square Foot

A scatter plot is used to analyze whether larger homes have a higher or lower rate per square foot:

```python
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()
```

This helps understand the relationship between property size and price per square foot.

---

## 📈 Visualizations

The project currently uses scatter plots to analyze:

* **Area vs Price**
* **Area vs Rate per Square Foot**

These visualizations make it easier to identify trends, relationships, and possible outliers in the real estate market.

---

## 🔍 Key Insights

The analysis can help answer important real-estate questions such as:

* Which areas are the most expensive?
* Which properties offer higher value per square foot?
* Does property size strongly influence price?
* Which BHK configuration has the highest average price?
* Does RERA approval have a relationship with property prices?
* Which builders have higher average property prices?
* How does construction status influence pricing?

The exact conclusions depend on the values present in `data.csv`.

---

## 🚀 Future Improvements

The project can be extended by adding:

* Correlation analysis
* Regression analysis
* Interactive dashboards using **Power BI** or **Plotly**
* More visualizations such as bar charts, box plots, and heatmaps
* Price prediction using Machine Learning
* Outlier detection
* Locality-wise price maps
* Feature importance analysis
* An interactive real-estate recommendation system

---

## 🏁 Conclusion

This project demonstrates how **Python and data analysis techniques can be used to extract meaningful insights from real-estate data**.

Through data cleaning, grouping, statistical analysis, and visualization, we can understand the major factors associated with property prices.

The project provides a foundation for moving from simple **exploratory data analysis** toward more advanced applications such as **real-estate price prediction, market intelligence, and property recommendation systems**.

> **Data tells the story — analysis helps us understand it. 📊🏠**

---

## 👨‍💻 Author

**Omkar Satpute**

This project was developed as part of a practical learning project in **Data Analysis using Python**.
