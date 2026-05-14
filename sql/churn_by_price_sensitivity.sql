SELECT
    charge_bucket,
    contract,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_percent
FROM customers
GROUP BY charge_bucket, contract
ORDER BY churn_rate_percent DESC;
