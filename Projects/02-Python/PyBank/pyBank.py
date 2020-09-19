from pathlib import Path
import csv

# Init variables
prev_month = 0
total_months = 0
net_pl = 0
delta = 0
sum_of_deltas = 0
average_delta = 0.0
max_profits_delta = ["",0]
max_losses_delta = ["",0]

# Path to File
file_path = Path(r"./Resources/budget_data.csv")

with open(file_path, 'r') as source:
    # Read file
    csv_reader = csv.reader(source, delimiter=",")
    # Iterate past header
    # 0: Month
    # 1: Profit/Losses
    csv_header = next(csv_reader)
    # Loop through the rest of the file to find max profit/losses deta
    for month in csv_reader:
        curr_month = int(month[1])
        net_pl += curr_month
        
        #Skip for 1st month
        if total_months != 0:
            delta = curr_month - prev_month
            sum_of_deltas += delta
            if delta >= max_profits_delta[1]:
                max_profits_delta = [month[0], delta]
            if delta <= max_losses_delta[1]:
                max_losses_delta = [month[0], delta]
        
        prev_month = curr_month
        total_months += 1

average_delta = round(sum_of_deltas / (total_months-1),2)

output = open(r"pybank_output.txt", "w")

output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write(f"Total Months: {total_months:,}\n")
output.write(f"Total: ${net_pl:,}\n")
output.write(f"Average  Change: ${average_delta:,}\n")
output.write(f"Greatest Increase in Profits: {max_profits_delta[0]} (${max_profits_delta[1]:,})\n")
output.write(f"Greatest Decrease in Profits: {max_losses_delta[0]} (${max_losses_delta[1]:,})\n")

output.close()

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months:,}")
print(f"Total: ${net_pl:,}")
print(f"Average  Change: ${average_delta:,}")
print(f"Greatest Increase in Profits: {max_profits_delta[0]} (${max_profits_delta[1]:,})")
print(f"Greatest Decrease in Profits: {max_losses_delta[0]} (${max_losses_delta[1]:,})")