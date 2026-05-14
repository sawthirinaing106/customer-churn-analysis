import pandas as pd

def clean_churn_data(input_path="data/customer_churn.csv",
                     output_path="data/customer_churn_cleaned.csv"):
    """
    Cleans the customer churn dataset:
    - Converts total_charges to numeric
    - Handles missing values
    - Standardizes categorical fields
    - Ensures correct data types
    """

    df = pd.read_csv(input_path)

    # Convert total_charges to numeric (coerce errors)
    df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")

    # Fill missing numeric values with median
    numeric_cols = ["monthly_charges", "total_charges", "tenure"]
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Standardize categorical values
    df["gender"] = df["gender"].str.title()
    df["partner"] = df["partner"].str.title()
    df["dependents"] = df["dependents"].str.title()
    df["phone_service"] = df["phone_service"].str.title()
    df["internet_service"] = df["internet_service"].str.title()
    df["contract"] = df["contract"].str.title()
    df["payment_method"] = df["payment_method"].str.title()
    df["churn"] = df["churn"].str.title()

    # Export cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to: {output_path}")


if __name__ == "__main__":
    clean_churn_data()
