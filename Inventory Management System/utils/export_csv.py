import pandas as pd

def export_to_csv(mysql_conn):
    try:
        query = "SELECT * FROM Products"
        df = pd.read_sql(query, mysql_conn)
        df.to_csv("inventory_data.csv", index=False)
        print("Inventory data exported to 'inventory_data.csv'")
    except Exception as e:
        print(f"Error exporting data: {e}")
