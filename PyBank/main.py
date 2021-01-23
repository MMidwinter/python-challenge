#Import OS to enable file paths across the OS
import os

#add the CSV module
import csv

#CSV file path
budget_path = os.path.join('Resources', 'budget_data.csv')

#Assign Dictionaries
Month = {}
ProfitLoss = {}

#Lists
#Month_Count = []
#ProfitAndLoss = []
#Profits = []
#Losses = []
#GreastestProfit = []
#GreatestLoss = []

#Variable for cleaned file
#cleaned_budget_data = os.path.join("cleaned_budget_data.csv")

#Defining the function
#def sum_profit_loss(budget_data):
        #month = str(budget_data[0])
        #profitloss = int(budget_data[1])

        #total_profit = 

# Reading the CSV
with open(budget_path) as csvfile:
    
    
    
    #Callout the delilmiter for dirty data
    #dirty_budget_data = csv.reader(csvfile, delimiter=',')
    
    #Removing blank lines
    #with open(cleaned_budget_data, "w") as cleaned_budget_data:
     #   writer = csv.writer(cleaned_budget_data)
      #  for row in csv.reader(dirty_budget_data):
       #     if row(any):
        #        writer.writerow(row)

    #Callout the delimiter
    read_budget_data = csv.reader(csvfile, delimiter=',')

    #print(read_budget_data)

    #Skipping the header
    #next(read_budget_data, None)

    #Test Reading the Header
    #budget_header = next(read_budget_data)
    #print(f"Budget Header: {budget_header}")

    for row in read_budget_data:
        
        #if not any(row):
            #continue
        
        #print(row)
        
        #Count the number of months and save it to the list
        Month_Count = len(list(read_budget_data))
        print(Month_Count)

        #Add Rows to Dictionaries
        PnL_dict = {'Month' : {row[0]},
                    'Profit and Loss' : {row[1]}}
        print(row)
        
        #if float(row[1]) > 0:
            #ProfitAndLoss += int(float(row[1]))
            #print(ProfitAndLoss)
        