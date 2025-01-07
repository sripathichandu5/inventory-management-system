import matplotlib.pyplot as plt

def visualize_data(mysql_conn):
    try:
        cursor = mysql_conn.cursor()
        query = "SELECT ProductName, Quantity FROM Products"
        cursor.execute(query)
        data = cursor.fetchall()

        products = [row[0] for row in data]
        quantities = [row[1] for row in data]

        plt.bar(products, quantities, color='skyblue')
        plt.xlabel("Products")
        plt.ylabel("Quantities")
        plt.title("Inventory Levels")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")
