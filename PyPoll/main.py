import os
import csv
import operator

csvpath = os.path.join("..","Resources","election_data.csv")

with open(csvpath, newline="") as csvread:
    csv_reader = csv.reader(csvread, delimiter=",")

    next(csv_reader)

    databank = []
    candidates = {}
#     net_amount = 0
#     avg_change = 0


    for row in csv_reader:
        databank.append(row)
        if not row[2] in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] = candidates[row[2]] + 1

    print(candidates)

    highest = sorted(candidates.items(), key=operator.itemgetter(1), reverse=True)
    
    print("Super Tuesday Results \n------------------------")
    print(f"Total Votes Casted: {len(databank)}\n------------------------")
    for candidate,count in candidates.items():
        print(f"{candidate}: {round(count*100/len(databank),2)}% ({count})")
    print(f"---------------------\nWinner\n--------------------")
    print(f"{highest[0][0]}")
#     print(f"Average Change: ${round(avg_change / (len(databank) - 1), 2)}")
#     print(f"Greatest Increase in Profits: {highest[0][0]} for ${highest[0][1]}")
#     print(f"Greatest Decrease in Profits: {highest[len(databank) -1][0]} for ${highest[len(databank) -1][1]}")

#append
#with open(file, "a") as myfile:
 #   myfile.write()