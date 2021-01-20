import csv
import os

# Adopted from course materials
electioncsv = os.path.join("Resources", "election_data.csv")

# Declare and initialize variables and lists
totalvotes = 0
candidates = []
candidatesvotes = []
Khanvotes = 0
Khanpercent = 0
Correyvotes = 0
Correypercent = 0
Livotes = 0
Lipercent = 0
OTooleyvotes = 0
Otooleypercent = 0
Winner = []

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

    # for row in csvreader:

    #     for counter in candidates:
    #         if row[2] == candidates[counter]:
    #             candidatesvotes[counter] += 1
        

# Calculate candidate percentage votes
Khanpercent = "{:.3%}".format(Khanvotes/totalvotes)
Correypercent = "{:.3%}".format(Correyvotes/totalvotes)
Lipercent = "{:.3%}".format(Livotes/totalvotes)
Otooleypercent = "{:.3%}".format(OTooleyvotes/totalvotes)

# for counter in candidatesvotes:
#     print(candidatesvotes[counter])

print("Election Results")
print("-----------------------------")
print("Total Votes :", totalvotes)
print("-----------------------------")
print(f'{candidates[0]}' ": ", Khanpercent, Khanvotes)
print(f'{candidates[1]}' " :", Correypercent, Correyvotes)
print(f'{candidates[2]}' " :", Lipercent, Livotes)
print(f'{candidates[3]}' " :", Otooleypercent, OTooleyvotes)
print("-----------------------------")
if Khanpercent > Correypercent and Khanpercent > Lipercent and Khanpercent > Otooleypercent:
    print(f'Winner : {candidates[0]}')
    Winner = candidates[0]
elif Correypercent > Khanpercent and Correypercent > Lipercent and Correypercent > Otooleypercent:
    print(f'Winner : {candidates[1]}')
    Winner = candidates[1]
elif Lipercent > Khanpercent and Lipercent > Correypercent and Lipercent > Otooleypercent:
    print(f'Winner : {candidates[2]}')
    Winner = candidates[2]
elif Otooleypercent > Khanpercent and Otooleypercent > Correypercent and Otooleypercent > Lipercent:
    print(f'Winner : {candidates[3]}')
    Winner = candidates[3]
print("-----------------------------")


# Adopted from class material
# Specify the file to write to
outputpath = os.path.join("analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputpath, 'w', newline='') as csvfile:
    
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Votes : " + str(totalvotes)])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([str(candidates[0]) + " :" + str(Khanpercent) + "   " + str(Khanvotes)])
    csvwriter.writerow([str(candidates[1]) + " :" + str(Correypercent) + "   " + str(Correyvotes)])
    csvwriter.writerow([str(candidates[2]) + " :" + str(Lipercent) + "   " + str(Livotes)])
    csvwriter.writerow([str(candidates[3]) + " :" + str(Otooleypercent) + "   " + str(OTooleyvotes)])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow(["Winner :" + str(Winner)])
    csvwriter.writerow(["-----------------------------"])