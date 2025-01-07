from db_connection import connect_mysql, connect_mongodb
from models.product import Product
from models.transaction import Transaction
from utils.data_analysis import analyze_inventory
from utils.visualization import visualize_data
from utils.export_csv import export_to_csv

def main_menu():
    print("\n=== Inventory Management System ===")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. Record Transaction")
    print("6. Analyze Inventory")
    print("7. Visualize Data")
    print("8. Export Inventory Data to CSV")
    print("9. Exit")
    print("===================================")
    choice = input("Enter your choice: ")
    return choice

def main():
    # Connect to databases
    mysql_conn = connect_mysql()
    mongodb_conn = connect_mongodb()

    if not mysql_conn:
        print("Failed to connect to MySQL. Exiting...")
        return
    if mongodb_conn is None:
        print("Failed to connect to MongoDB. Exiting...")
        return

    # Initialize modules
    product_module = Product(mysql_conn)
    transaction_module = Transaction(mysql_conn)

    while True:
        choice = main_menu()

        if choice == "1":
            print("\n=== Add Product ===")
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            supplier_id = input("Enter Supplier ID: ")
            product_module.add_product(product_id, name, category, quantity, price, supplier_id)

        elif choice == "2":
            print("\n=== Update Product Quantity ===")
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter New Quantity: "))
            product_module.update_product_quantity(product_id, quantity)

        elif choice == "3":
            print("\n=== Update Product Price ===")
            product_id = input("Enter Product ID: ")
            price = float(input("Enter New Price: "))
            product_module.update_product_price(product_id, price)

        elif choice == "4":
            print("\n=== Delete Product ===")
            product_id = input("Enter Product ID to delete: ")
            product_module.delete_product(product_id)

        elif choice == "5":
            print("\n=== Record Transaction ===")
            transaction_id = input("Enter Transaction ID: ")
            product_id = input("Enter Product ID: ")
            trans_type = input("Enter Transaction Type (Purchase/Sale): ")
            quantity = int(input("Enter Quantity: "))
            transaction_module.record_transaction(transaction_id, product_id, trans_type, quantity)

        elif choice == "6":
            print("\n=== Analyze Inventory ===")
            analyze_inventory(mysql_conn)

        elif choice == "7":
            print("\n=== Visualize Data ===")
            visualize_data(mysql_conn)

        elif choice == "8":
            print("\n=== Export Inventory Data ===")
            export_to_csv(mysql_conn)

        elif choice == "9":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close database connections
    if mysql_conn:
        mysql_conn.close()
        print("MySQL connection closed.")
    if mongodb_conn:
        print("MongoDB connection closed.")

if __name__ == "__main__":
    main()
