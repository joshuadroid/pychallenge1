import csv
import os
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

# For Loop to count all the votes using a dictionary
for row in data:
    total_count += 1
    if row[2] in vote_count.keys():
        vote_count[row[2]] += 1
    else:
        vote_count[row[2]] = 1

# Start printing the results
print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {total_count}")
print(f"-----------------------")
winner = 0
winner_name = ""


# Export text file with results
output_path = os.path.join("Analysis", "Financial_Analysis.csv")

with open(output_path, 'w') as csvfile:
    
    csvfile.write(f"Election Results\n")
    csvfile.write(f"-----------------------\n")
    csvfile.write(f"Total Votes: {total_count}\n")
    csvfile.write(f"-----------------------\n")

    # For Loop to determine the winner and output everyone's results
    for x in vote_count.keys():
        percentage = (int(vote_count[str(x)]) / total_count) * 100
        print(f"{x} {percentage:.3f}% ({vote_count[str(x)]})")
        csvfile.write(f"{x} {percentage:.3f}% ({vote_count[str(x)]})")
        if percentage > winner:
            winner = percentage
            winner_name = x

    csvfile.write(f"-----------------------\n")
    csvfile.write(f"Winner: {winner_name}\n")
    csvfile.write(f"-----------------------")

print(f"-----------------------")
print(f"Winner: {winner_name}")
print(f"-----------------------")