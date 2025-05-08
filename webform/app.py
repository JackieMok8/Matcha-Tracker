# doe eerst in terminal: cd "C:\Users\MokJackie(Calco)\Documents\Hard-skill assignments\Matcha Tracker Project\webform"
# gebruik daarna: python app.py om te activeren in console

from flask import Flask, render_template, request, redirect
import mysql.connector
import json  # ← voor data naar JavaScript

app = Flask(__name__)

# MySQL verbinding
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="matcha_tracker"
)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    cursor = db.cursor()
    sql = """
        INSERT INTO cafes (name, city, address, visiting_date, order_taken, price, rating, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        request.form['name'],
        request.form['city'],
        request.form['address'],
        request.form['visiting_date'],
        request.form['order_taken'],
        request.form['price'],
        request.form['rating'],
        request.form['notes']
    )
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return redirect('/')

@app.route('/cafes')
def cafes():
    cursor = db.cursor(dictionary=True)
    
    # Query om het aantal bezoeken per café per week op te halen
    cursor.execute("""
        SELECT 
            id, name, city, address, visiting_date, order_taken, price, rating, notes
        FROM cafes
        ORDER BY visiting_date DESC
    """)


    cafes = cursor.fetchall()
    cursor.close()
    
    return render_template('cafes.html', cafes=cafes)

@app.route('/dashboard')
def dashboard():
    cursor = db.cursor(dictionary=True)

    # Haal cafés op
    cursor.execute("SELECT * FROM cafes ORDER BY visiting_date DESC")
    cafes = cursor.fetchall()

    # Haal week-data op voor grafiek
    cursor.execute("""
        SELECT 
            YEAR(visiting_date) AS year,
            WEEK(visiting_date, 1) AS week_number,
            SUM(price) AS total_spent,
            COUNT(*) AS total_visits
        FROM cafes
        GROUP BY year, week_number
        ORDER BY year, week_number
    """)
    results = cursor.fetchall()  # <-- Resultaten ophalen NA de query
    cursor.close()

    # Nu kun je veilig lists maken
    weeks = [f"Week {row['week_number']} ({row['year']})" for row in results]
    totals = [float(row['total_spent']) for row in results]
    visits = [row['total_visits'] for row in results]

    return render_template(
        "dashboard.html",
        cafes=cafes,
        weeks=json.dumps(weeks),
        totals=json.dumps(totals),
        visits=json.dumps(visits)
    )

    return render_template("dashboard.html", cafes=cafes, weeks=json.dumps(weeks), totals=json.dumps(totals), visits=json.dumps(visits))

@app.route('/analytics')
def analytics():
    cursor = db.cursor(dictionary=True)

    # Haal week-data op voor grafiek
    cursor.execute("""
        SELECT 
            YEAR(visiting_date) AS year,
            WEEK(visiting_date, 1) AS week_number,
            SUM(price) AS total_spent,
            COUNT(*) AS total_visits
        FROM cafes
        GROUP BY year, week_number
        ORDER BY year, week_number
    """)
    results = cursor.fetchall()
    cursor.close()

    # Voor de grafiek:
    weeks = [f"Week {row['week_number']} ({row['year']})" for row in results]
    totals = [float(row['total_spent']) for row in results]
    visits = [row['total_visits'] for row in results]

    return render_template(
        "analytics.html",
        weeks=json.dumps(weeks),
        totals=json.dumps(totals),
        visits=json.dumps(visits)
    )

    return render_template("analytics.html", weeks=json.dumps(weeks), totals=json.dumps(totals))


@app.route('/delete/<int:cafe_id>')
def delete_cafe(cafe_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM cafes WHERE id = %s", (cafe_id,))
    db.commit()
    cursor.close()
    return redirect('/dashboard')

    # Prepare data for chart
    weeks = [f"Week {row[0]}" for row in results]
    totals = [float(row[1]) for row in results]

    return render_template("dashboard.html", weeks=json.dumps(weeks), totals=json.dumps(totals))

@app.route('/edit/<int:cafe_id>', methods=['GET'])
def edit(cafe_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cafes WHERE id = %s", (cafe_id,))
    cafe = cursor.fetchone()
    cursor.close()
    return render_template("edit.html", cafe=cafe)


@app.route('/update/<int:cafe_id>', methods=['POST'])
def update(cafe_id):
    cursor = db.cursor()
    sql = """
        UPDATE cafes
        SET name=%s, city=%s, address=%s, visiting_date=%s,
            order_taken=%s, price=%s, rating=%s, notes=%s
        WHERE id=%s
    """
    values = (
        request.form['name'],
        request.form['city'],
        request.form['address'],
        request.form['visiting_date'],
        request.form['order_taken'],
        request.form['price'],
        request.form['rating'],
        request.form['notes'],
        cafe_id
    )
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    return redirect('/dashboard')

# 👇 Dit moet altijd helemaal onderaan staan
if __name__ == '__main__':
    app.run(debug=True)
