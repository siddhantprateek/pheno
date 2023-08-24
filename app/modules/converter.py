import json
import csv
import os

def csv_to_json():
    current_directory = os.getcwd()
    csv_file_path = f'{current_directory}/data/input.csv' 
    json_file_path = f'{current_directory}/data/output.json' 
    
    csv_data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csv_data.append(row)

    with open(json_file_path, 'w') as json_file:
        json.dump(csv_data, json_file, indent=4)
