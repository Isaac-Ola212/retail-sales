from etl import extract, transform, load

def main():
    print("Starting ETL pipeline")
    extracted = extract()
    cleaned_path = transform()
    loaded = load()
    print("ETL pipeline finished")

if __name__ == "__main__":
    main()
