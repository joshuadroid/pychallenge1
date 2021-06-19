import csv

path = "Resources/budget_data.csv"
data = []

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for x in csvreader:
        data.append(x)

count = 0
for row in data:
    count += 1

print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {count}")

total = 0
for row in data:
    total += row[1]

print(f"Total: ${total}")

