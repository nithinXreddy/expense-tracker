from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nithin@23",
    database="expense_db"
)

@app.route("/", methods=["GET", "POST"])
def index():
    cursor = db.cursor()

    if request.method == "POST":
        title = request.form["title"]
        amount = request.form["amount"]
        type_ = request.form["type"]

        query = "INSERT INTO expenses (title, amount, type) VALUES (%s, %s, %s)"
        values = (title, amount, type_)
        cursor.execute(query, values)
        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    return render_template("index.html", expenses=data)

if __name__ == "__main__":
    app.run(debug=True)