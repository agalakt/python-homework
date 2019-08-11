from pathlib import Path
import csv

csvpath = Path('budget_data.csv')

months = 0
total_amount = 0
average_change = 0
min_profit = 0
max_profit = 0

line_num = 0

with open(csvpath, 'r') as csvfile:
    print(type(csvfile))
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(type(csvreader))
    line_num += 1
    header = next(csvreader)
    print(f"Financial Analysis")
    print(f"-----------------------") 

#months script

    data = list(csvreader)
    row_count = len(data)
    print(f"Total Months: {row_count}")
    
#total amount script

    for row in csvreader: 
        total_amount += int(row[1])
        
    print (f"Total: {total_amount}")
    
        
    
    
#average change script

    print(f"Average Change: ${total_amount / row_count}")

#greatest increase

    max_profit = max(int(row[1]))
    print(f"Greatest Increase in Profits: {max_profit}")
    
    
#greatest decrease

    min_proft = min(int(row[1]))
    print(f"Greatest Decrease in Profits: {min_profit}")
    