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
value_list = []

#Using a for loop to calculate everything
for row in data:
    #calculate count and total
    count += 1
    total += int(row[1])
    print(row[1])
    # change = int(row[1]) - int(row[1]-1)
    # print(change)








## TODO Get this average change working!!

## pseudo code it.
## run a for loop to determine each change
## capture all values in a list
## sum the values of the list
## divide by the length of the list

# print(value_list)

# def compare(list):
#     return_list = []
#     n = 0
#     for x in list:
#         if len(list) == n+1:
#             print(return_list)
#             break

#         n += 1
#         return_list.append(change)

# compare(value_list)



#print statement of everything
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
average = 0
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")


# TODO: get change loop working (above)
# TODO: export text file with results