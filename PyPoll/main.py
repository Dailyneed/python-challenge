# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the path where the file is residing
csvpath = os.path.join('Resources', 'election_data.csv')

# Declare variables and intialize
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        # Count the total votes in the dataset
        total_votes = total_votes + 1

        # candidates name is listed in row 2 of the dataset
        candidate_name = row[2]

        # count votes for each candidate
              
        if "Charles Casper Stockham" == candidate_name:
            charles_votes = charles_votes + 1

        if "Diana DeGette" == candidate_name:
                diana_votes = diana_votes + 1

        if "Raymon Anthony Doane" == candidate_name:
                    raymon_votes = raymon_votes + 1
        
        # Find percentage votes for each candidate
        charles_percent = (charles_votes / total_votes) * 100

        diana_percent = (diana_votes / total_votes) * 100

        raymon_percent = (raymon_votes / total_votes) * 100

        # To find the winner of the election, zip list together to form dictionary 
    if charles_votes > diana_votes and charles_votes > raymon_votes:
        winner = "Charles Casper Stockham"
    elif diana_votes > charles_votes and diana_votes > raymon_votes:
        winner = "Diana DeGette"
    else:
        winner ="Raymon Anthony Doane" 
       
        
 

# print to terminal
print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print("--------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

# write to file
# Specify the file to write to
output_path = os.path.join("Analysis", "election_result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w+') as file:

    # Initialize writer
    file.write(f"Election Results\n")
    file.write("\n")
    file.write(f"-----------------------------------\n")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("\n")
    file.write(f"-------------------------------------\n")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})\n")
    file.write(f"Raymon Antony Doane: {raymon_percent:.3f}% ({raymon_votes})\n")
    file.write(f"-------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"-------------------------------------\n")

    

