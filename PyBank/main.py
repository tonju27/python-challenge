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
        
        if int(row[1]) > maxprofit:
            maxprofit = int(row[1])
        
        if int(row[1]) < minprofit:
            minprofit = int(row[1])
        
        profit.append(int(row[1]))
        
        # if totalmonths != 1:
        #     previousrow = int(row[1])
        #     changetotal = int(previousrow) - int(row[1])
        
        # profit = int(row[1])
         
        # if profit > 0:
        #     totalprofit += profit
        # elif profit < 0:
        #     totalloss += profit
    
    for counter in range(len(profit)-1):
        changeprofit.append(int(profit[counter+1]) - int(profit[counter]))

    # changetotal = totalprofit - totalloss
    # avgchange = changetotal/totalmonths
    
    # maxprofit = max(int(row[1])
    
# minprofit = min(int(row[1])
   
print(totalmonths)
print(nettotal)
print(sum(changeprofit)/totalmonths)
print(maxprofit)
print(minprofit)
print(max(profit))
print(min(profit))
