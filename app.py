from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    try:
        # 1. Connect to the LOCAL fridge (the database)
        conn = sqlite3.connect('kumon_progress.db')
        
        # 2. Read the 'progress' table we created in Step 1
        df = pd.read_sql_query("SELECT * FROM progress", conn)
        conn.close()
        
        # 3. Convert to HTML for the front end
        html_table = df.to_html(classes='table table-striped table-hover', index=False)
    except Exception as e:
        html_table = f"Database is empty or error occurred: {e}. Did you run update_data.py?"

    return render_template("index.html", table_html=html_table)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)