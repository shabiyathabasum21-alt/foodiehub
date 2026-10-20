import mysql.connector
from collections import Counter

db = mysql.connector .connect(
    host="127.0.0.1" ,
    user="root",
    password="password",
    database="foodiehub"
   
)
cur = db.cursor()
cur.execute("SELECT items FROM orders")
rows = cur .fetchall()
db.close()

counts = Counter()

for (items,) in rows:
    for dish in items.split(","):
        counts[dish.strip().title()] += 1

print("------ORDER REPORT ------")
print("Total orders:", len(rows))
print("Dishes ordered:")

for dish, n in counts .most_common():
    print(repr(dish),"-",n)