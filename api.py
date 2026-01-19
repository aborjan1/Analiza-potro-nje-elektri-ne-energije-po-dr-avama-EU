from flask import Flask, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

DB = "eu_energy.db"

@app.route("/countries")
def countries():
    conn = sqlite3.connect(DB)
    df = pd.read_sql("SELECT DISTINCT country FROM energy_consumption", conn)
    conn.close()
    return jsonify(df["country"].tolist())

@app.route("/energy")
def all_energy():
    conn = sqlite3.connect(DB)
    df = pd.read_sql("SELECT * FROM energy_consumption", conn)
    conn.close()
    return jsonify(df.to_dict(orient="records"))

@app.route("/energy/<country>")
def energy_country(country):
    conn = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT * FROM energy_consumption WHERE country=?",
        conn,
        params=(country.upper(),)
    )
    conn.close()
    return jsonify(df.to_dict(orient="records"))

@app.route("/energy/<country>/<int:year>")
def energy_country_year(country, year):
    conn = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT * FROM energy_consumption WHERE country=? AND year=?",
        conn,
        params=(country.upper(), year)
    )
    conn.close()
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
