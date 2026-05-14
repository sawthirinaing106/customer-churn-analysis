import pandas as pd

def churn_feature_engineering(input_path="data/customer_churn_cleaned.csv",
                              output_path="data/customer_churn_features.csv"):
    """
    Creates engineered features for churn analysis:
    - Binary churn flag
    - Tenure groups
    - Monthly charge buckets
    - High-risk customer indicator
    """

    df = pd.read_csv(input_path)

    # Binary churn flag
    df["churn_flag"] = df["churn"].apply(lambda x: 1 if x == "Yes" else 0)

    # Tenure groups
    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["0-12 months", "12-24 months", "24-48 months", "48+ months"],
        include_lowest=True
    )

    # Monthly charge buckets
    df["charge_bucket"] = pd.cut(
        df["monthly_charges"],
        bins=[0, 50, 80, 120],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )

    # High-risk customer indicator
    df["high_risk"] = df.apply(
        lambda row: 1 if (row["churn_flag"] == 1 and row["monthly_charges"] > 90) else 0,
        axis=1
    )

    # Export engineered dataset
    df.to_csv(output_path, index=False)
    print(f"Feature-engineered dataset saved to: {output_path}")


if __name__ == "__main__":
    churn_feature_engineering()
