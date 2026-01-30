import csv

def read_csv(filepath):
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            yield row
