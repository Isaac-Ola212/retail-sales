import pandas as pd
from pathlib import Path

def extract(raw_dir: str = "dataset/raw-data", out_dir: str = "dataset/processed"):
    raw_path = Path(raw_dir)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    files = {
        "sales": "sales-data-set.csv",
        "features": "Features-data-set.csv",
        "stores": "stores-data-set.csv",
    }

    data = {}
    for key, fname in files.items():
        f = raw_path / fname
        if not f.exists():
            raise FileNotFoundError(f"Expected raw file not found: {f}")
        df = pd.read_csv(f)
        out_file = out_path / f"{key}.csv"
        df.to_csv(out_file, index=False)
        data[key] = out_file

    print(f"Extracted files written to {out_path}")
    return data

if __name__ == "__main__":
    extract()
