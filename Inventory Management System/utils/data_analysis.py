import pandas as pd

def analyze_inventory(mysql_conn):
    try:
        query = "SELECT * FROM Products"
        df = pd.read_sql(query, mysql_conn)
        print("\nInventory Analysis:")
        print(df.describe())
    except Exception as e:
        print(f"Error analyzing inventory: {e}")
