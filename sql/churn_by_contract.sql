SELECT 
    contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        AVG(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100,
    2) AS churn_rate_percent
FROM customers
GROUP BY contract
ORDER BY churn_rate_percent DESC;