from __future__ import annotations
from csv import DictReader
from pathlib import Path

import csv
import sys

def read_csv_rows(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1) 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)