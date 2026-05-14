SELECT 
    internet_service,
    contract,
    charge_bucket,
    COUNT(*) AS total_customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(AVG(churn_flag) * 100, 2) AS churn_rate_percent
FROM customers
GROUP BY internet_service, contract, charge_bucket
ORDER BY churn_rate_percent DESC;
