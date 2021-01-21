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
nettotalformat = 0
averageformat = 0
averagechange = 0
maxformat = 0
minformat = 0

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

# Format variables with $ sign
nettotalformat = "${:.0f}".format(nettotal)
averagechange = sum(changeprofit)/(totalmonths-1)
averageformat = "${:.2f}".format(averagechange)
maxformat = "${:.0f}".format(max(changeprofit))
minformat = "${:.0f}".format(min(changeprofit))

print("Financial Analysis")
print("-------------------------------------------------")
print(f'Total months:           {totalmonths}')
print(f'Total:           {nettotalformat}')
print(f'Average change:  {averageformat}')
print(f'Greatest increase in profits:  {month[maxindex]}  {maxformat}')
print(f'Greatest decrease in profits:  {month[minindex]}  {minformat}')

# Adopted from class material
# Specify the file to write to
outputpath = os.path.join("analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputpath, 'w', newline='') as csvfile:
    
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------"])
    # csvwriter.writerow(["Total months, Total, Average change, Greatest increase, Greatest decrease")
    csvwriter.writerow(["Total months:" + "    " + str(totalmonths)])
    csvwriter.writerow(["Total:" + "           " + str(nettotalformat)])
    csvwriter.writerow(["Average change:" + "  " + str(averageformat)])
    csvwriter.writerow(["Greatest increase in profits:" + "  " + str(month[maxindex]) + "  " + str(maxformat)])
    csvwriter.writerow(["Greatest decrease in profits:" + "  " + str(month[minindex]) + "  " + str(minformat)])

