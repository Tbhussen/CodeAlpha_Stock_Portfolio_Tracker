# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:56:43 2024

@author: Tamim_Hussein
"""
import requests
from prettytable import PrettyTable

def Get_Price (symbol):
    # You can get API_KEY from: https://www.alphavantage.co/support/#api-key
    API_Key = 'GWQY5SJRJM2L019E'
    Base_url = 'https://www.alphavantage.co/query'
    # Specifying parameters
    params = {
        'function' : 'GLOBAL_QUOTE',
        'symbol' : symbol,
        'apikey' : API_Key}
    response = requests.get(Base_url, params = params)
    data = response.json()
    
    # Check if response is valid
    if 'Global Quote' not in data:
        print(f'Error fetching data for {symbol}')
        return None
    # Changing the stock_price to float value
    stock_price = data['Global Quote']['05. price']
    stock_price = float(stock_price)
    return stock_price

def add_Stock():
    print()
    symbol = input("Enter Stock symbol: ")
    shares = int(input("Enter the shares amount: "))
    # Check if stock is present in portfolio:
    if symbol not in stock_data:
        stock_data[symbol] = shares
        print(f"{symbol} added successfully")
    # If stock is present update the shares
    else:
        action = input("Do you want to do add or subtract shares : ")
        manage_shares(symbol, action, shares)
    
def remove_Stock(symbol):
    print()
    stock_data.pop(symbol)
    print("Removing Stock...\n")
    print(f"{symbol} has been removed from the portfolio")
    
def Display_Portfolio():
    print()
    print("This might take few seconds...")
    table = PrettyTable()
    table.field_names = ["Symbol","Shares","Stock_Value (in $)"]
    summ = 0.0
    
    # Calculating the stock_value of each type of stock
    for symbol in stock_data:
        shares = stock_data[symbol]
        total_value = Get_Price(symbol) * shares
        summ += total_value
        # Displaying it with 2 decimal places
        total_value = f"{total_value:.2f}"
        # Adding a new row to the table
        table.add_row([symbol, shares, total_value])
    # Printing pretty_table
    print(table)
    # Total value in the portfolio
    print("Total Value of Stock : ", summ) 

def manage_shares(symbol, action, shares):
    # Adding to the shares
    if action == "add":
        stock_data[symbol] += shares
    # Subtracting from the shares
    elif action == "subtract":
        stock_data[symbol] -= shares
    else:
        print(f"{action} not recognized")
    print(f"{symbol} shares updated!")

# MAIN
# Dictionary containing the stock and the corresponding number of shares
stock_data = {}
print("\t\t\tWelcome to Stock Portfolio Tracker")
print("\t\t\t----------------------------------")

# Looping the program until specified by the user
while(True):
        
    print("What do you want to do:")
    print("1. Add Stock\n2. Remove Stock\n3. Display Portfolio\n4. Exit Program")
    
    # Input the key to the action to be made
    choice = int(input("Choose number from the list: "))
    if choice == 1:
        add_Stock()
        print("----------------------------------------")
        
    elif choice == 2:
        i = 1
        for symbol in stock_data:
            print(i,". ", symbol, sep = "")
            i += 1
        removed_stock = input("Which stock do you want to remove: ")
        remove_Stock(removed_stock)
        print("----------------------------------------")
        
    elif choice == 3:
        Display_Portfolio()
        print("----------------------------------------")
        
    elif choice == 4:
        print("\t\tThank you for using Stock Portfolio Tracker\n\t\t\t\t\tHave a nice day!")
        break
    else:
        print("No such choice..choose from the numbers in the menu")
        continue