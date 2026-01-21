import pandas as pd
from pathlib import Path

def transform(processed_dir: str = "dataset/processed", out_file: str = "dataset/processed/cleaned_sales_data.csv"):
    p = Path(processed_dir)
    sales_f = p / "sales.csv"
    features_f = p / "features.csv"
    stores_f = p / "stores.csv"

    if not sales_f.exists():
        raise FileNotFoundError(f"Missing sales file: {sales_f}")

    sales = pd.read_csv(sales_f)

    # Attempt to read features and stores if present
    if features_f.exists():
        features = pd.read_csv(features_f)
        # common merge keys often are Store and Date
        if "Date" in sales.columns and "Date" in features.columns:
            features["Date"] = pd.to_datetime(features["Date"], errors="coerce")
            sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")
            sales = sales.merge(features, how="left", on=["Store", "Date"]) if {"Store"}.issubset(sales.columns) else sales
        else:
            sales = sales.merge(features, how="left", on="Store") if "Store" in sales.columns and "Store" in features.columns else sales

    if stores_f.exists() and "Store" in sales.columns:
        stores = pd.read_csv(stores_f)
        sales = sales.merge(stores, how="left", on="Store")

    # Basic cleaning
    # Convert Date to datetime if present
    if "Date" in sales.columns:
        sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")

    # Fill obvious missing numeric columns with 0
    numeric_cols = sales.select_dtypes(include=["number"]).columns
    sales[numeric_cols] = sales[numeric_cols].fillna(0)

    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    sales.to_csv(out_file, index=False)
    print(f"Transformed data written to {out_file}")
    return out_file

if __name__ == "__main__":
    transform()
