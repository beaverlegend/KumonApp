from flask import Flask, render_template
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

# --- INFRASTRUCTURE SETUP ---
# This checks if we are running on Render; otherwise, it uses your local folder.
base_dir = os.path.abspath(os.path.dirname(__file__))
if os.environ.get('RENDER'):
    # This path matches the 'Mount Path' you'll set in Render's dashboard
    DB_PATH = '/opt/render/project/src/data/kumon_progress.db'
else:
    # Local path for development
    DB_PATH = os.path.join(base_dir, 'kumon_progress.db')
# ----------------------------

@app.route("/")
def index():
    try:
        # Connect using the dynamic path
        conn = sqlite3.connect(DB_PATH)
        
        df = pd.read_sql_query("SELECT * FROM progress", conn)
        conn.close()
        
        html_table = df.to_html(classes='table table-striped table-hover', index=False)
    except Exception as e:
        html_table = f"Database error: {e}. Check if {DB_PATH} exists."

    return render_template("index.html", table_html=html_table)

if __name__ == "__main__":
    # Use port from environment (Render/Railway set this automatically) 
    # or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)