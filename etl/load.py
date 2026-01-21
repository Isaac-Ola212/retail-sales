from pathlib import Path
import shutil

def load(clean_file: str = "dataset/processed/cleaned_sales_data.csv", target_dir: str = "dataset/clean-data"):
    src = Path(clean_file)
    dst_dir = Path(target_dir)
    if not src.exists():
        raise FileNotFoundError(f"Clean file not found: {src}")
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    shutil.copy2(src, dst)
    print(f"Loaded cleaned data to {dst}")
    return dst

if __name__ == "__main__":
    load()
