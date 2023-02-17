import csv
import json

with open('cycles.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    
output = json.dumps(rows, indent=2, sort_keys=True)
print(output)
