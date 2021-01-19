import csv
import os

# Adopted from course materials
budgetcsv = os.path.join("Resources", "budget_data.csv")

# Declare and initialize variables and lists
totalmonths = 0
nettotal = 0
changeprofit = []
profit = []
month = []

# Open and read csv
with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    header = next(csvreader)

    

    for row in csvreader:
        # Count number of months and sum Profit/Loss column
        totalmonths += 1
        nettotal = nettotal + int(row[1])
        
        # Append Profit/Loss to profit list
        profit.append(int(row[1]))
        
        # Profit change starts in year 2 so omit year 1 in month list
        # TA advice on slack 1/18/21
        if totalmonths !=1:
            month.append(str(row[0]))

        # Append change in profit to changeprofit
        # -1 prevents counter+1 from going out of range
    for counter in range(len(profit)-1):
        changeprofit.append(int(profit[counter+1]) - int(profit[counter]))

# Index of maximum change
maxindex = changeprofit.index(max(changeprofit))

#  Index of minimum change
minindex = changeprofit.index(min(changeprofit))

print("Financial Analysis")
print("-----------------------------------")
print(f'Total months : {totalmonths}')
print("Total : ", "$", nettotal)
print(f'Average change : ${round(sum(changeprofit)/(totalmonths-1),2)}')
print(f'Greatest increase in profits : {month[maxindex]} ${max(changeprofit)}')
print(f'Greatest decrease in profits : {month[minindex]} ${min(changeprofit)}')

# Adopted from class material
# Specify the file to write to
outputpath = os.path.join("..", "analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputpath, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow('Financial Analysis')
    csvwriter.writerow('---------------------------')
    csvwriter.writerow(f'Total months : {totalmonths}')
    csvwriter.writerow("Total : ", "$", nettotal)
    csvwriter.writerow(f'Average change : ${round(sum(changeprofit)/(totalmonths-1),2)}')
    csvwriter.writerow(f'Greatest increase in profits : {month[maxindex]} ${max(changeprofit)}')
    csvwriter.writerow(f'Greatest decrease in profits : {month[minindex]} ${min(changeprofit)}')

