import sqlite3
import pandas as pd

def print_capstone_results():
    try:
        # Connect to the fresh database
        conn = sqlite3.connect('capstone.db')
        
        # Query the data loaded by the Loading_Agent
        query = "SELECT * FROM sales_records"
        df = pd.read_sql_query(query, conn)
        
        print("\n" + "="*50)
        print("CAPSTONE DATA PIPELINE: FINAL OUTPUT")
        print("="*50)
        
        if df.empty:
            print("The database is connected but no records were found.")
        else:
            # Display the data formatted for your report
            print(df.to_string(index=False))
            
        print("="*50 + "\n")
        conn.close()
        
    except Exception as e:
        print(f"Error: Could not read capstone.db. Details: {e}")

if __name__ == "__main__":
    print_capstone_results()