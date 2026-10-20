from flask import Flask, jsonify, request 
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="foodiehub"
    )

@app.route("/menu")
def menu():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM menu_items")
    items = cur.fetchall()
    db.close()
    return jsonify(items)

@app.route("/order", methods=["POST"])
def order():
    data = request.get_json()
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO orders (items, address) VALUES (%s, %s)",
        (data["items"], data["address"])
    )
    db.commit()
    db.close()
    return jsonify({"message": "Order saved"})

app.run(debug=True)