import csv
import os

file = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Create lists for each column
Ballot_ID = []
County = []
Candidate = []

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        # Add Ballot ID into first list
        Ballot_ID.append(row[0])

        # Add County to second list
        County.append(row[1])

        # Add Candidate to third list
        Candidate.append(row[2])

# Delete Headers
del Ballot_ID[0]
del County[0]
del Candidate[0]

# Retrive total votes
Total_Votes = len(Ballot_ID)

# Distiniguish unique list of candidate names
Candidates_Set = set(Candidate)

# Create lists for each candidate's votes
can1 = []
can2 = []
can3 = []

# Append Candidate's lists with their votes
for x in Candidate:
    if x == "Charles Casper Stockham":
        can1.append("Charles Casper Stockham")

    if x == "Diana DeGette":
        can2.append("Diana DeGette")

    if x == "Raymon Anthony Doane":
        can3.append("Raymon Anthony Doane")

# Retrive the number of votes per candidate
can1_len = len(can1)
can2_len = len(can2)
can3_len = len(can3)

# Calculate the percentage of votes each candidate recieved
Casper_perc = ((can1_len / Total_Votes) * 100)
Casper_perc = str(round(Casper_perc, 3))

Diana_perc = ((can2_len / Total_Votes) * 100)
Diana_perc = str(round(Diana_perc, 3))

Raymon_perc = ((can3_len / Total_Votes) * 100)
Raymon_perc = str(round(Raymon_perc, 3))

# Create a dictionary with the results to retrieve the winner
results = {'Charles Casper Stockham': can1_len, 'Diana DeGrette': can2_len, 'Raymon Anthony Doane': can3_len}

# Retrieve winner
winner = max(results, key=results.get)

# print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes))
print("-------------------------")
print("Charles Casper Stockham: " + Casper_perc + "% (" + str(can1_len) + ")")
print("Diana DeGette: "+ Diana_perc + "% (" + str(can2_len) + ")")
print("Raymon Anthony Doane: " + Raymon_perc + "% (" + str(can3_len) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Output info into txt file
output_file = os.path.join("analysis", "PyPoll_Output.txt")

with open (output_file, "w") as f:
    f.write("Election Results" + "\n")
    f.write("-------------------------" + "\n")
    f.write("Total Votes: " + str(Total_Votes) + "\n")
    f.write("-------------------------" + "\n")
    f.write("Charles Casper Stockham: " + Casper_perc + "% (" + str(can1_len) + ")" + "\n")
    f.write("Diana DeGette: "+ Diana_perc + "% (" + str(can2_len) + ")" + "\n")
    f.write("Raymon Anthony Doane: " + Raymon_perc + "% (" + str(can3_len) + ")" + "\n")
    f.write("-------------------------" + "\n")
    f.write("Winner: " + winner + "\n")
    f.write("-------------------------" + "\n")

