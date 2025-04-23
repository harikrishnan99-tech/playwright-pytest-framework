import os
import csv

def read_csv_data(*filenames):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    all_data = []

    for filename in filenames:
        file_path = os.path.join(base_path, "data", filename)
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            all_data.extend(list(reader))
    return all_data

def read_text_values(filename, key=None):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "data", filename)
    values = {}

    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                values[row["text"].lower()] = row["value"]

        if key:
            return values.get(key.lower(), "")
        return values

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return {}
