class Transaction:
    def __init__(self, mysql_conn):
        self.conn = mysql_conn

    def record_transaction(self, transaction_id, product_id, trans_type, quantity):
        try:
            cursor = self.conn.cursor()
            # Update product quantity based on transaction type
            if trans_type == "Purchase":
                update_query = "UPDATE Products SET Quantity = Quantity + %s WHERE ProductID = %s"
            elif trans_type == "Sale":
                update_query = "UPDATE Products SET Quantity = Quantity - %s WHERE ProductID = %s"
            else:
                print("Invalid transaction type!")
                return

            # Insert transaction
            transaction_query = """
                INSERT INTO Transactions (TransactionID, ProductID, Type, Quantity)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(transaction_query, (transaction_id, product_id, trans_type, quantity))
            cursor.execute(update_query, (quantity, product_id))
            self.conn.commit()
            print(f"{trans_type} transaction recorded successfully!")
        except Exception as e:
            print(f"Error recording transaction: {e}")
