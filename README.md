CUSTOMER-CHURN-ANALYSIS/
│
├── data/
│   ├── customer_churn.csv
│   ├── customer_churn_cleaned.csv
│   └── customer_churn_features.csv
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── scripts/
│   ├── clean_churn_data.py
│   └── churn_feature_engineering.py
│
├── sql/
│   ├── churn_rate.sql
│   ├── churn_by_contract.sql
│   ├── churn_by_tenure_group.sql
│   ├── high_risk_segments.sql
│   ├── customer_lifetime_value.sql
│   ├── payment_method_churn.sql
│   ├── monthly_charges_churn.sql
│   ├── senior_citizen_churn.sql
│   ├── churn_by_price_sensitivity.sql
│   ├── churn_by_internet_service.sql
│   ├── early_life_churn.sql
│   ├── high_value_customer_churn.sql
│   ├── churn_by_payment_behavior.sql
│   ├── senior_vs_non_senior_by_contract.sql
│   ├── multi_factor_churn_segments.sql
│   └── high_risk_flag_analysis.sql
│
├── visuals/
│   ├── churn_rate.png
│   ├── churn_by_contract.png
│   ├── churn_by_tenure.png
│   └── churn_heatmap.png
│
└── README.md

Data Cleaning.. 
Performed using clean_churn_data.py:
Converted incorrect data types
Filled missing values
Standardized categorical fields
Ensured numerical consistency
Exported a clean dataset for analysis

Feature Engineering...
Performed using churn_feature_engineering.py:
Churn_flag (binary churn indicator)
tenure_group (0–12, 12–24, 24–48, 48+ months)
charge_bucket (Low, Medium, High)
high_risk (high‑charge customers with churn behavior)
These features improve segmentation and predictive insights.

Exporatory Data Analysis(EDA)
The notebook churn_analysis.ipynb includes:
Dataset overview
Churn distribution
Churn by contract type
Churn by tenure group
Correlation heatmap
High‑risk customer identification
Visual storytelling with Seaborn & Matplotlib

SQL Segmentation Analysis
The sql/ folder contains production‑style SQL queries for:
Churn rate
Contract‑based churn
Tenure‑based churn
High‑risk customer segments
Lifetime value analysis
Payment behavior
Multi‑factor segmentation
Early‑life churn detection
These queries simulate real‑world analytics work in telecom and subscription industries.

Key Insights
Month‑to‑month contracts have the highest churn rate.
Customers in their first 12 months are most likely to churn.
High monthly charges strongly correlate with churn.
Electronic check payment method shows elevated churn risk.
High‑risk customers can be identified early using engineered features.

Tech Stack
Python (Pandas, NumPy, Seaborn, Matplotlib)
SQL
Jupyter Notebook
Git & GitHub
VS Code

Author
Saw Thi Ri Naing  
Data Analyst | SQL | Python | Visualization | Business Insights
