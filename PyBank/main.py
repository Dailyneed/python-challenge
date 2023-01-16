# Import the os module, this will allow us to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Python program to get average of a list
# Using mean()
  
# importing mean()
from statistics import mean

# Specify the path where the file is residing
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set variables and values
totalmonths = 0
net_profit = 0
monthly_change = 0
profit_loss_list = []
monthly_change_list = []
result = 0 
maxAnswer = 0
maxDate = ''
minAnswer = 0
minDate = ''


# Open and read CSV file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    proceeds = dict()

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        amount = float(row[1])
        date = str(row[0])
       
        #row[0: 'Date'], row[1:'Profit/loss']
        # Count the total of months in the dataset
        totalmonths = totalmonths + 1

        # Calculate the net total amount of profit/loss over the entire period
        net_profit = net_profit + amount

        # Calculate changes in profit/losses over the entire period and then the average of those changes

        if len(profit_loss_list) == 0:
            profit_loss_list.append(amount)
        else:
            monthly_change = amount - profit_loss_list[-1]
            monthly_change_list.append(monthly_change)
            proceeds[date] = monthly_change
            profit_loss_list.append(amount)
            

    # caluclate avergae profilt loss
    result = mean(monthly_change_list)


    # Find the greatest increase in profit (date and amount) over the entire period
    maxAnswer = max(proceeds.values())
   

    for key,value in  proceeds.items():
        if maxAnswer == value:
            maxDate = key
          

      # Find the greatest decrease in profit (date and amount) over the entire period
    minAnswer = min (proceeds.values())
 

    for key,value in proceeds.items():
        if minAnswer == value:
           minDate = key

    
        

# print to terminal
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {str(totalmonths)}")
print(f"Total: $ {str(net_profit)}")
print(f"Average change: $ {result:.2f}")
print(f"Greatest increase in Profits: {str(maxDate)} $ ({maxAnswer})")
print(f"Greatest decrease in Profits: {str(minDate)} $ ({minAnswer})")

        
# write to file
# Specify the file to write to
output_path = os.path.join("Analysis", "budget_result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w+') as file:

    # Initialize writer
    file.write(f"Financial Analysis\n")
    file.write(f"-----------------------------------\n")
    file.write(f"Total Months: {totalmonths}\n")
    file.write(f"Total: $ {str(net_profit)}\n")
    file.write(f"Average change: $ {result:.2f} \n")
    file.write(f"Greatest increase in Profits: {str(maxDate)} $ ({maxAnswer})\n")
    file.write(f"Greatest decrease in Profits: {str(minDate)} $ ({minAnswer})\n")
 



