import csv

#declare path
path = "Resources/budget_data.csv"
data = []

#open and read the csv file, commit to a list
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for x in csvreader:
        data.append(x)

#set up and commit for loop, looking for count
#added in if statements to get the greatest increase and decrease
count = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""
average_list = []

#Using a for loop to calculate everything
for row in data:
    #calculate count and total
    count += 1
    total += int(row[1])

    #if statement to see if a value is higher or lower than a previous
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        greatest_increase_month = str(row[0])
    elif int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
        greatest_decrease_month = str(row[0])




# for i in data:
#     month = data[i]
#     next_month = data[i+1]
#     change = month / next_month
#     print(f"{month} / {next_month} will equal {change}")
    


#print statement of everything
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")


# TODO: get change loop working (line 41)
# TODO: export text file with results