import csv
filename='data/simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row= next(reader)
    print(header_row)