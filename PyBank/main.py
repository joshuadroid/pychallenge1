import csv
import os
#declare path
PATH = "Resources/budget_data.csv"
PROFIT_COL = 1
MONTH_COL = 0

#open and read the csv file, commit to a list
with open(PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    data = []
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
profit_list = []
return_list = []
previous_profit = int(data[0][PROFIT_COL])

#Using a for loop to calculate everything
for row in data:
    #calculate count and total
    count += 1
    current_profit = int(row[PROFIT_COL])
    total += current_profit

    # calculcate the change and store in current_change
    current_change = current_profit - previous_profit

    #if statement to see if a value is higher or lower than a previous
    if int(current_change) > greatest_increase:
        greatest_increase = int(current_change)
        greatest_increase_month = str(row[MONTH_COL])
    elif int(current_change) < greatest_decrease:
        greatest_decrease = int(current_change)
        greatest_decrease_month = str(row[MONTH_COL])

    profit_list.append(int(current_change))
    previous_profit = current_profit

#calculate the average change
average = sum(profit_list) / len(profit_list)

#print statement of everything
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")


# Export text file with results
output_path = os.path.join("Analysis", "Financial_Analysis.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Count", count])
    csvwriter.writerow(["Total", total])
    csvwriter.writerow(["Average Change", average])
    csvwriter.writerow(["Greatest Increase in Profits Month", greatest_increase_month])
    csvwriter.writerow(["Greatest Increase in Profits", greatest_increase])
    csvwriter.writerow(["Greatest Decrease in Profits Month", greatest_decrease_month])
    csvwriter.writerow(["Greatest Decrease in Profits", greatest_decrease])