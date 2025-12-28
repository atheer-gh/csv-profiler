import csv

def read_csv_rows(file_path: str):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"Error reading file: {e}")
        return []