import csv
from collections import Counter

#data
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
#mean

for x in range(len(file_data)):
    n_num = file_data[x][1]
    new_data.append(float(n_num))


length = len(new_data)
total = 0
for x in new_data:
    total = total + x

mean = total/length
print("Mean/Average is  : " + str(mean))

#median
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()
print(new_data)

if n % 2 == 0:
    num1 = float(new_data[n//2])

    num2 = float(new_data[n//2 - 1])
    median = (num1+ num2)/2
else:
    median = new_data[n//2]

print("Median is  : " + str(median))

#mode
for y in range(len(file_data)):
    n_num = file_data[y][1]
    new_data.append(float(n_num))
data = Counter(new_data)
modeDataRange = {"50-60": 0, "60-70": 0, "70-80": 0}

for height, occurance in data.items():
    if 50 < float(height) < 60:
        modeDataRange["50-60"] += occurance
    elif 60 < float(height) < 70:
        modeDataRange["60-70"] += occurance
    elif 70 < float(height) < 80:
        modeDataRange["70-80"] += occurance

modeRange, modeOccurance = 0,0
for range, occurance in modeDataRange.items():
    if occurance > modeOccurance:
        modeRange, modeOccurance =  [int(range.split("-")[0]), int(range.split("-")[1])], occurance
mode = float((modeRange[0] + modeRange[1])/2)
print("Mode is : " + str(mode))



