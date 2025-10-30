import argparse
import sys
import os
from extract import extract_data
from transform import transform_data
from load import load_data

sys.path.append(os.path.dirname(__file__))


def main():
    parser = argparse.ArgumentParser(description="ETL Pipeline")
    parser.add_argument("--input", "-i", required=True, help="Input CSV file link")
    parser.add_argument(
        "--table", "-t", default="mental_health", help="Database table name"
    )

    args = parser.parse_args()

    raw_data = extract_data(args.input)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, args.table)


if __name__ == "__main__":
    main()
