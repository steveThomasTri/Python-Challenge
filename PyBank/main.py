import os
import csv
import operator

csvpath = os.path.join("..","Resources","budgetdata.csv")

with open(csvpath, newline="") as csvread:
    csv_reader = csv.reader(csvread, delimiter=",")

    next(csv_reader)

    databank = []
    net_amount = 0
    avg_change = 0


    for row in csv_reader:
        databank.append([row[0],int(row[1])])
        net_amount += int(row[1])

    for x in range(len(databank)-1):
        avg_change += (int(databank[x+1][1]) - int(databank[x][1]))

    highest = sorted(databank, key=operator.itemgetter(1), reverse=True)
    
    print("Financial Analysis \n------------------------")
    print(f"Total Months: {len(databank)}")
    print(f"Total: ${net_amount}")
    print(f"Average Change: ${round(avg_change / (len(databank) - 1), 2)}")
    print(f"Greatest Increase in Profits: {highest[0][0]} for ${highest[0][1]}")
    print(f"Greatest Decrease in Profits: {highest[len(databank) -1][0]} for ${highest[len(databank) -1][1]}")

#append
#with open(file, "a") as myfile:
 #   myfile.write()