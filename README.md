# CodeAlpha_Stock_Portfolio_Tracker
## Brief Discription
Python Programming Task. Here, we implement financial API, alpha vantage, to create a personal stock portfolio tracker
## Detailed Discription
This is a Python program that allows users to manage a simple stock portfolio by adding, removing, and displaying stocks along with their current values in USD. The program fetches real-time stock prices using the Alpha Vantage API.

### Features

`Add Stocks`: Add stocks by symbol and specify the number of shares owned. If the stock already exists, you can choose to add or subtract shares.

`Remove Stocks`: Remove stocks from the portfolio by specifying the stock symbol.

`Display Portfolio`: View the portfolio with a detailed table of symbols, shares, and the current market value of each stock.

`Fetch Live Stock Prices`: The program fetches up-to-date stock prices via the Alpha Vantage API, ensuring accurate valuations.

`Calculate Total Portfolio Value`: Displays the total value of the portfolio based on current stock prices.

### Requirements

_Required Python libraries:_

`requests`: for making API requests to Alpha Vantage

`prettytable`: for displaying portfolio data in a table format

### Code Structure

`Get_Price(symbol)`: Fetches the current price of a stock symbol from Alpha Vantage.

`add_Stock()`: Adds a new stock or updates the shares of an existing stock.

`remove_Stock(symbol)`: Removes a stock from the portfolio.

`Display_Portfolio()`: Displays all stocks in a formatted table and calculates the total portfolio value.

`manage_shares(symbol, action, shares)`: Manages the addition or subtraction of shares for an existing stock.

_Project Done_
