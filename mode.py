import csv
from collections import Counter

with open("height-weight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]

    new_data.append(float(n_num))

data = Counter(new_data)
mode_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for height, occurrence in data.items():
    if 50 < float(height) < 60:
        mode_range["50-60"] += occurrence
    elif 60 < float(height) < 70:
        mode_range["60-70"] += occurrence
    elif 70 < float(height) < 80:
        mode_range["70-80"] += occurrence

modeRange, modeOccurrence = 0, 0

for range, occurrence in mode_range.items():
    if occurrence > modeOccurrence:
        modeRange, modeOccurrence = [int(range.split("-")[0]), int(range.split("-")[1])]
    
mode = float((modeRange[0] + modeRange[1])/2)
print("Mode is: " + str(mode))