# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

#Function to read a CSV file to list of lists
def read_csv_to_list (file_path):
    """read_csv_to_list
    -------------------
    Parameter:
    file_path - Path object containing path to a CSV file
    -------------------
    Return content of the CSV file without its header
    """
    csv_list = []
    with open(file_path, 'r') as file:
        file_reader = csv.reader(file, delimiter=",")
        next(file_reader)
        for line in file_reader:
            csv_list.append(line)
    return csv_list

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path(r"./Resources/menu_data.csv")
sales_filepath = Path(r"./Resources/sales_data.csv")

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
menu = read_csv_to_list(menu_filepath)   
# @TODO: Read in the sales data into the sales list
sales = read_csv_to_list(sales_filepath)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sales_line in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    #line_item_id = line[0]
    #date = line[1]
    #credit_card_number = line[2]
    quantity = int(sales_line[3])
    menu_order = sales_line[4]
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_order in report:
        report[menu_order]["01-Count"] += quantity 
    else:
        report[menu_order] = {"01-Count" : quantity,
                            "02-Revenue" : 0,
                            "03-COGS" : 0,
                            "04-Profit" : 0}
    
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_line in menu:
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = menu_line[0]
        price = float(menu_line[3])
        cost = float(menu_line[4])
        
        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_order.lower() == item.lower():
            
            # @TODO: Print out matching menu data
            print(f"{menu_order} price: {price}, cost: {cost}")
            
            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_order]["02-Revenue"] += quantity * price
            report[menu_order]["03-COGS"] += quantity * cost
            report[menu_order]["04-Profit"] += quantity * profit
            
        # @TODO: Else, the sales item does not equal any of the item in the menu data, therefore no match
        else:
            continue

    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f"There are {row_count:,} transactions")

# @TODO: Write out report to a text file (won't appear on the command line output)
output_filepath = Path(r"./Output.txt")
with open(output_filepath, "w") as output:
    for item in report:
        out_line = f"{item} " + str(report[item]) + "\n"
        output.write(out_line)