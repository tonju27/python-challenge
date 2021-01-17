import csv
import os


budgetcsv = os.path.join("Resources", "budget_data.csv")

totalmonths = 0
nettotal = 0

# Open and read csv
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    header = next(csvreader)
    for counter in csvfile:
        totalmonths += 1
        nettotal += float(csvfile[1])
print(totalmonths, nettotal)

