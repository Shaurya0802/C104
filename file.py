import csv

with open('height-weight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

from collections import Counter
new_data = "whitehatjr"
data = Counter(new_data)
print(data)
value = data.values()
keys = data.keys()
print(value)
print(keys)
