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
    print(len(Month))
    
    #Print the total Profit.Losses
    print(sum(map(int, ProfitLoss)))

    #calculate the average change
    AverageChange = [sum(MoMChange) / len(MoMChange)]
    
    #Print the Average Change
    print(sum(MoMChange) / len(MoMChange))

    #print(max(map(int, ProfitLoss)))
    #print(min(ProfitLoss))

    print(max(MoMChange))
    print(min(MoMChange))
        

#for row in budget_path:
 #   print(row)
