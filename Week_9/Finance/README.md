# Finance

## Getting Started
This project consists of a Flask web application that allows users to register, log in, buy and sell stocks and view their transaction history. To run this application on your machine, you need to have Python and Flask installed. After cloning the repository, navigate to the root directory of the project in your terminal and execute the following command to start the Flask application:
```
flask run
```

After that, open your web browser and navigate to http://localhost:5000 to access the application.

## Background
This program was completed as part of the CS50 course offered by Harvard University. The goal of the project was to develop a web application that would allow users to manage their portfolios of stocks by buying, selling and viewing their transaction history.

## Implementation Details
The web application is built using Python and Flask. The data for the stocks is obtained using the IEX Cloud API, and the user data is stored in a SQLite database. The website uses HTML, CSS and Bootstrap for the front-end.

The application provides the following routes:

- /register: allows users to create a new account by providing a unique username and a password.
- /login: allows users to log in to their account.
- /logout: allows users to log out of their account.
- /quote: allows users to obtain the latest price of a stock by entering its symbol.
- /buy: allows users to buy stocks by specifying the stock symbol and the number of shares.
- /sell: allows users to sell stocks they own by specifying the stock symbol and the number of shares they want to sell.
- /history: allows users to view their transaction history.

## Example Usage
To register a new user account, navigate to http://localhost:5000/register and fill out the registration form. After that, you can log in to your account by navigating to http://localhost:5000/login.

To buy a stock, enter its symbol and the number of shares you want to buy in the http://localhost:5000/buy form and click the "Buy" button.

To sell a stock, select its symbol from the drop-down menu in the http://localhost:5000/sell form and enter the number of shares you want to sell.

To view your transaction history, navigate to http://localhost:5000/history.

### Author
Joaquim Luzia.

Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
