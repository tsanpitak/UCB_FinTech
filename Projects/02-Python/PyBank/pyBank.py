import pandas as pd

total_months = 0
net_pl = 0
delta = 0
sum_of_deltas = 0
average_delta = 0
max_profits_delta = ["",0]
max_losses_delta = ["",0]
last_month_pl = 0

# Read CSV file into DataFrame
pl_data = pd.read_csv(r"Resources/budget_data.csv")

# # of months = # of rows
total_months = len(pl_data)
net_pl = sum(pl_data[r"Profit/Losses"])

#initialize first month as basis to calculate delta
last_month_pl = pl_data.loc[0,r"Profit/Losses"]

for i in range(1,total_months):
    # Calculate delta
    delta = pl_data.loc[i,r"Profit/Losses"] - last_month_pl
    # Keep track of total delta
    sum_of_deltas += delta
    # Is this max profit?
    if delta >= max_profits_delta[1]:
        max_profits_delta = [pl_data.loc[i,r"Date"], delta]
    # Is this max loss?
    if delta <= max_losses_delta[1]:
        max_losses_delta = [pl_data.loc[i,r"Date"], delta]
    # Prep for next month
    last_month_pl = pl_data.loc[i,r"Profit/Losses"]
        
average_delta = round(sum_of_deltas / (total_months -1),2)
        
print("\nFinancial Analysis")
print("----------------------------")
print("Total Months: ", total_months)
print("Total: $", net_pl)
print("Average  Change: $", average_delta)
print(f"Greatest Increase in Profits: {max_profits_delta[0]} (${max_profits_delta[1]})")
print(f"Greatest Decrease in Profits: {max_losses_delta[0]} (${max_losses_delta[1]})")