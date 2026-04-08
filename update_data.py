import pandas as pd
import sqlite3

# Your Google CSV Link
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRiARRgc9tMVcfsuObBT54sXtFn2bfClsTVavm6As3py8YNXfXCRlf0_aPu7KN04soXYN4XiFZs478v/pub?gid=649881926&single=true&output=csv"

def sync_from_google():
    print("Fetching data from Google...")
    # 1. Read from Google
    df = pd.read_csv(SHEET_URL)
    
    # 2. Connect to SQLite (this creates kumon_progress.db if it doesn't exist)
    conn = sqlite3.connect('kumon_progress.db')
    
    # 3. Save the data to a table called 'progress'
    # 'replace' means every time we run this, it updates with the newest Google data
    df.to_sql('progress', conn, if_exists='replace', index=False)
    
    conn.close()
    print("Success! Database 'kumon_progress.db' updated.")

if __name__ == "__main__":
    sync_from_google()
