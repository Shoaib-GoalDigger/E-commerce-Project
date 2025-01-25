from users import add_user, view_users, delete_user
from products import add_product, view_products, delete_product, update_product

def main_menu():
    while True:
        print("\nE-Commerce Management")
        print("1. User Management")
        print("2. Product Management")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            product_menu()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def user_menu():
    while True:
        print("\nUser Management")
        print("1. Add User")
        print("2. View Users")
        print("3. Delete User")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            add_user(user_id, name, email)
        elif choice == "2":
            view_users()
        elif choice == "3":
            user_id = input("Enter User ID to delete: ")
            delete_user(user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

def product_menu():
    while True:
        print("\nProduct Management")
        print("1. Add Product")
        print("2. View Products")
        print("3. Delete Product")
        print("4. Update Product")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            description = input("Enter Product Description: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Product Stock: "))
            add_product(product_id, name, description, price, stock)
        elif choice == "2":
            view_products()
        elif choice == "3":
            product_id = input("Enter Product ID to delete: ")
            delete_product(product_id)
        elif choice == "4":
            product_id = input("Enter Product ID to update: ")
            field = input("Enter field to update (name/description/price/stock): ")
            value = input("Enter new value: ")
            # Convert value to appropriate type
            if field in ["price", "stock"]:
                value = float(value) if field == "price" else int(value)
            update_product(product_id, field, value)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
