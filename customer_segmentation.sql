--Project 2: Customer Segmentation Analysis
--Tool: MySQL

USE customer_segmentation;

-- View sample data
SELECT * FROM customers LIMIT 5;

-- Customers per cluster
SELECT Cluster, COUNT(*) AS customer_count
FROM customers
GROUP BY Cluster
ORDER BY Cluster;

-- Average income and spending per cluster
SELECT 
    Cluster,
    ROUND(AVG(Annual_Income), 2) AS avg_income,
    ROUND(AVG(Spending_Score), 2) AS avg_spending
FROM customers
GROUP BY Cluster
ORDER BY Cluster;

-- Gender distribution by cluster
SELECT 
    Cluster,
    Gender,
    COUNT(*) AS count
FROM customers
GROUP BY Cluster, Gender
ORDER BY Cluster;

-- High value customers
SELECT *
FROM customers
WHERE Annual_Income > 80
  AND Spending_Score > 70;
