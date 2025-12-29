import csv
from pathlib import Path

def read_csv_rows(file_path: str | Path) -> list[dict]:
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Sorry, I couldn't find the file at: {path}")
    try:
        
        with open(path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        
        raise RuntimeError(f"An error happened while reading the CSV: {e}")