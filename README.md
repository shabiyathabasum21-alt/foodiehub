# FoodieHub

Food ordering web app built with HTML, CSS, JavaScript, Python (Flask) and MySQL, with an ETL order report.

## Screenshots


![Home](screenshots/home.png)




![Cart](screenshots/cart.png)




![Report](screenshots/report.png)



## How it works
- Menu is loaded from MySQL through a Flask API
- Users add dishes to a cart and place an order
- Orders are saved in MySQL
- etl.py reads the orders and prints a report

## How to run
1. Run schema.sql in MySQL
2. Put your MySQL password in app.py and etl.py
3. Run: py app.py
4. Open index.html with Live Server
