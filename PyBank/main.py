import csv
import os


budgetcsv = os.path.join("Resources", "budget_data.csv")

totalmonths = 0
nettotal = 0
avgchange = 0

totalprofit = 0
totalloss - 0
nettotal = 0
profit = 0




# Open and read csv
with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)
    # skip header
    header = next(csvreader)

    

    for row in csvreader:
        totalmonths += 1
        nettotal = sum(int(row[1])
        
        profit = int(row[1])
         
        if profit > 0:
            totalprofit += profit
        elif profit < 0:
            totalloss += profit
            
    nettotal = totalprofit - totalloss
    avgchange = (nettotal - totalloss)/totalmonths
    maxprofit = 0
    maxprofit = max(int(row[1]]))
    minprofit = 0
    minprofit = min(int(row[1]))
   
print(totalmonths)
print(nettotal)
print(avgchange)
print(maxprofit)
print(minprofit)

