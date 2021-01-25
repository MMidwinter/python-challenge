#Import OS to enable file paths across the OS
import os

#add the CSV module
import csv

#CSV file path
budget_path = os.path.join('..', 'Resources', 'budget_data.csv')

#open the file
with open(budget_path) as csvfile:

    #Specify the Delimiter
    budgetreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    header = next(budgetreader)
    #print(f"Header: {header}")

    #print(budgetreader)
    #Assign the initial previous row
    previous_row = next(budgetreader)

    #lists to store data
    Month = [previous_row[0]]
    ProfitLoss = [previous_row[1]]
    PreviousProfitLoss = [0]
    MoMChange = []
    Total = []
    AverageChange = []
    GreatestProfit = [int(0)]
    GreatestProfitMonth = []
    GreatestLoss = [int(0)]
    GreatestLossMonth = []


    #Read each row in the CSV
    for row in budgetreader:
        #print(row)

         #Apped Row Data to Lists
        #Append the Month
        Month.append(row[0])
        
        #Append Profit and Loss as a Int
        ProfitLoss.append((int(row[1])))
        #print(ProfitLoss)
        
        if int(previous_row[1]) != int(row[1]):
            #print(previous_row[1])

            #calculate the change in cells
            change = int(row[1]) - int(previous_row[1])
            
            #print(change)
            MoMChange.append(change)
            #print(MoMChange)
            
            previous_row = row

    #Print the number of Months
    #print(len(Month))
    MonthCount = len(Month)
    #print(MonthCount)

    #Print the total Profit.Losses
    #print(sum(map(int, ProfitLoss)))
    Total = sum(map(int, ProfitLoss))
    Total = "${:.0f}".format(Total)
    #print(Total)

    #find months for greatest profit and loss
    #GreatestProfitMonth = MoMChange.index(max(MoMChange))
    #My Tutor David Sosa helped me use the index to identify the correct months.
    GreatestProfitMonth = Month[MoMChange.index(max(MoMChange)) + 1]
    #print(GreatestProfitMonth)

    GreatestLossMonth = Month[MoMChange.index(min(MoMChange)) + 1]
    #print(GreatestLossMonth)

    #calculate the average change
    #print(sum(MoMChange) / len(MoMChange))
    AverageChange = sum(MoMChange) / len(MoMChange)
    AverageChange = "${:.2f}".format(AverageChange)
    #print(AverageChange)

    #Calculate the max profit and record it
    #print(max(MoMChange))
    GreatestProfit = max(MoMChange)
    GreatestProfit = "${:.0f}".format(GreatestProfit)
    #print(GreatestProfit)

    #Calculate the greatest lost and record it
    #print(min(MoMChange))
    GreatestLoss = min(MoMChange)
    GreatestLoss = "${:.0f}".format(GreatestLoss)
    #print(GreatestLoss)

    #Print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {MonthCount}")
    print(f"Total : {Total}")
    print(f"Average Change: {AverageChange}")
    print(f"Greatest Increase in Profits: {str(GreatestProfitMonth)} ({GreatestProfit})")
    print(f"Greatest Decrease in Profits: {str(GreatestLossMonth)} ({GreatestLoss})")

    f = open("PyBank Analysis.txt", "w")
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {MonthCount}\n")
    f.write(f"Total : {Total}\n")
    f.write(f"Average Change: {AverageChange}\n")
    f.write(f"Greatest Increase in Profits: {str(GreatestProfitMonth)} ({GreatestProfit})\n")
    f.write(f"Greatest Decrease in Profits: {str(GreatestLossMonth)} ({GreatestLoss})\n")
    f.close()

#for row in budget_path:
 #   print(row)
