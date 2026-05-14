SELECT
    customer_id,
    monthly_charges,
    tenure,
    (monthly_charges * tenure) AS lifetime_value
FROM customers
ORDER BY lifetime_value DESC;
