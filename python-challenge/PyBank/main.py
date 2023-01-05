import csv
import os

budget_file = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

Date = []
Profit_Loss = []

with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    for row in csvreader:
        # Add Date into first list
        Date.append(row[0])

        # Add Profit/Loss into second list
        Profit_Loss.append(row[1])

# Delete Headers
del Date[0]
del Profit_Loss[0]

# Find total number of months included in the dataset
Total_Months = len(Date)

# Iterate through the Profit / Loss list to change str to int
for i in range(0, len(Profit_Loss)):
    Profit_Loss[i] = int(Profit_Loss[i])

# Find net total amount in Profit / Losses over entire period
Total_Amount = sum(Profit_Loss)

# Create empty list for the changes in profit 
Changes = []

# Iterate to append the calcuated change in profit to a new list
for x in range(0, len(Profit_Loss) - 1):
    Changes.append(Profit_Loss[x+1] - Profit_Loss[x])

# Calcuate the average change
Average_Change = sum(Changes) / len(Changes)

# Format as string and round decimal
Average_Change = str(round(Average_Change, 2))

# Retrieve greatest increase in changes list and correlate to its index
Greatest_Increase = max(Changes)
z = Changes.index(Greatest_Increase)

# Retrieve greatest decrease in changes list and correlate to its index
Greatest_Decrease = min(Changes)
zz = Changes.index(Greatest_Decrease)

# Define that dates at the indicies with the greatest increases and decreases in change
Greatest_Increase_Date = Date[z]
Greatest_Decrease_Date = Date[zz]

# Print with casting
print("Finacial Analysis")
print("----------------------------")
print("Total Months: " + str(Total_Months))
print("Total: $" + str(Total_Amount))
print("Average Change: $" + str(Average_Change))
print("Greatest Increase in Profits: " + str(Greatest_Increase_Date) + " ($" + str(Greatest_Increase) + ")" )
print("Greatest Decrease in Profits: " + str(Greatest_Decrease_Date) + " ($" + str(Greatest_Decrease) + ")" )

# Output info into txt file
output_file = os.path.join("analysis", "PyBank_Output.txt")

# f = open("PyBank_Output.txt", "w")

with open (output_file, "w") as f: 
    f.write("Finacial Analysis" + "\n")
    f.write("----------------------------" + "\n")
    f.write("Total Months: " + str(Total_Months) + "\n")
    f.write("Total: $" + str(Total_Amount) + "\n")
    f.write("Average Change: $" + str(Average_Change) + "\n")
    f.write("Greatest Increase in Profits: " + str(Greatest_Increase_Date) + " ($" + str(Greatest_Increase) + ")" + "\n" )
    f.write("Greatest Decrease in Profits: " + str(Greatest_Decrease_Date) + " ($" + str(Greatest_Decrease) + ")" + "\n")


