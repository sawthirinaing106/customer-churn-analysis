SELECT
    tenure_group,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_percent
FROM customers
WHERE tenure <= 12
GROUP BY tenure_group
ORDER BY churn_rate_percent DESC;
