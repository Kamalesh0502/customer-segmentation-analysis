import pandas as pd
df =pd.read_csv(r"D:\DATA ANLYTICS PROJECTS\Project 2\Data\Mall_Customers.csv")
df.head()
df.info()

print(df.describe())
print(df["Gender"].value_counts())


x=df[["Annual Income (k$)","Spending Score (1-100)"]]
print(x.head())

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=5,random_state=42)
kmeans.fit(x)

df["Cluster"]=kmeans.labels_
print(df.head())

import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(
           df["Annual Income (k$)"],
           df["Spending Score (1-100)"],
           c=df["Cluster"],
           s=60
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation")

plt.show()

df.to_csv("customer_segmentation_with_clusters.csv", index=False)
