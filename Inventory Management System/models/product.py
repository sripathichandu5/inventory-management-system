class Product:
    def __init__(self, mysql_conn):
        self.conn = mysql_conn

    def add_product(self, product_id, name, category, quantity, price, supplier_id):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Products (ProductID, ProductName, Category, Quantity, Price, SupplierID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (product_id, name, category, quantity, price, supplier_id))
            self.conn.commit()
            print(f"Product {name} added successfully!")
        except Exception as e:
            print(f"Error adding product: {e}")

    def update_product_quantity(self, product_id, quantity):
        try:
            cursor = self.conn.cursor()
            query = "UPDATE Products SET Quantity = %s WHERE ProductID = %s"
            cursor.execute(query, (quantity, product_id))
            self.conn.commit()
            print("Product quantity updated successfully!")
        except Exception as e:
            print(f"Error updating product quantity: {e}")

    def update_product_price(self, product_id, price):
        try:
            cursor = self.conn.cursor()
            query = "UPDATE Products SET Price = %s WHERE ProductID = %s"
            cursor.execute(query, (price, product_id))
            self.conn.commit()
            print("Product price updated successfully!")
        except Exception as e:
            print(f"Error updating product price: {e}")

    def delete_product(self, product_id):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM Products WHERE ProductID = %s"
            cursor.execute(query, (product_id,))
            self.conn.commit()
            print("Product deleted successfully!")
        except Exception as e:
            print(f"Error deleting product: {e}")
