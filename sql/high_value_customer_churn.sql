SELECT
    customer_id,
    monthly_charges,
    tenure,
    (monthly_charges * tenure) AS lifetime_value
FROM customers
WHERE churn_flag = 1
ORDER BY lifetime_value DESC;
