SELECT 
    COUNT(CASE WHEN churn = 'Yes' THEN 1 END) * 1.0 /
    COUNT(*) AS churn_rate
FROM customers;
