import csv
data = []

# Set Path and Open File
path = "Resources/election_data.csv"
with open(path, 'r') as csvfile:
    
    # Convert to csv reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read in the header row
    csv_header= next(csvreader)

    # Go through the data and put it in a list
    for x in csvreader:
        data.append(x)


total_count = 0
vote_count = {}

for row in data:
    total_count += 1
    if row[2] in vote_count.keys():
        vote_count[row[2]] += 1
    else:
        vote_count[row[2]] = 1

print(total_count)
print(vote_count)


## TODO need to find percentages and winner


print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {total_count}")
print(f"-----------------------")

# for x in vote_count.keys():
#     list = vote_count.items()
#     x = list[0]
#     y = list[1]
#     print(f"{x} : {round(y / total_count, 2)}% ({y}) ")

print(f"-----------------------")
# print(f"Winner: {winner}")
print(f"-----------------------")