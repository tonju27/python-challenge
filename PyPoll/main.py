import csv
import os

# Adopted from course materials
electioncsv = os.path.join("Resources", "election_data.csv")

# Declare and initialize variables and lists
totalvotes = 0
candidates = []
Khanvotes = 0
Khanpercent = 0
Correyvotes = 0
Correypercent = 0
Livotes = 0
Lipercent = 0
OTooleyvotes = 0
Otooleypercent = 0
Khanrounded = 0

# Open and read csv
with open(electioncsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    header = next(csvreader)

    for row in csvreader:
        totalvotes += 1

        # Append unique list. Syntax from geeksforgeeks.org
        if row[2] not in candidates:
            candidates.append(row[2])

        # Total votes for each candidate
        if row[2] == "Khan":
            Khanvotes += 1
        elif row[2] == "Correy":
            Correyvotes += 1
        elif row[2] == "Li":
            Livotes += 1
        elif row[2] == "O'Tooley":
            OTooleyvotes += 1


# Calculate candidate percentage votes
Khanpercent = round((Khanvotes/totalvotes),2) * 100
# Khanrounded = round((Khanpercent),3)
Correypercent = round((Correyvotes/totalvotes),2) * 100
Lipercent = round((Livotes/totalvotes),2) * 100
Otooleypercent = round((OTooleyvotes/totalvotes),2) * 100



print("Total Votes :", totalvotes)
print(f'{candidates[0]}' ": ", Khanpercent, "% ", Khanvotes)
print(f'{candidates[1]}' " :", Correypercent, "% ", Correyvotes)
print(f'{candidates[2]}' " :", Lipercent, "% ", Livotes)
print(f'{candidates[3]}' " :", Otooleypercent, "% ", OTooleyvotes)
