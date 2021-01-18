import csv
import os


budgetcsv = os.path.join("Resources", "budget_data.csv")

totalmonths = 0
nettotal = 0
avgchange = 0
totalprofit = 0
totalloss = 0
changeprofit = []
profit = []
minprofit = 0
maxprofit = 0
previousrow=0
# counter = 0

# Open and read csv
with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)
    # skip header
    header = next(csvreader)

    

    for row in csvreader:
        totalmonths += 1
        nettotal = nettotal + int(row[1])
        
        # if int(row[1]) > maxprofit:
        #     maxprofit = int(row[1])
        
        # if int(row[1]) < minprofit:
        #     minprofit = int(row[1])
        
        profit.append(int(row[1]))
        
            
    for counter in range(len(profit)-1):
        changeprofit.append(int(profit[counter+1]) - int(profit[counter]))

   
print(f'"Total months : " {totalmonths}')
print("Total : ", nettotal)
print(f'"Average change : " {round(sum(changeprofit)/(totalmonths-1)),2}')
print(f'"Greatest increase in profits : " {max(changeprofit)}')
print(f'"Greatest decrease in profits : {min(changeprofit)}')


