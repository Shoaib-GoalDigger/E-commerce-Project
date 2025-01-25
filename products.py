import json

# File to store product data
PRODUCT_FILE = "products.json"

# Load products from file
def load_products():
    try:
        with open(PRODUCT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save products to file
def save_products(products):
    with open(PRODUCT_FILE, 'w') as file:
        json.dump(products, file, indent=4)

# Add a new product
def add_product(product_id, name, description, price, stock):
    products = load_products()
    if product_id in products:
        print("Product ID already exists!")
    else:
        products[product_id] = {
            "name": name,
            "description": description,
            "price": price,
            "stock": stock
        }
        save_products(products)
        print("Product added successfully!")

# View all products
def view_products():
    products = load_products()
    if not products:
        print("No products found!")
    else:
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: ₹{details['price']}, Stock: {details['stock']}")

# Delete a product
def delete_product(product_id):
    products = load_products()
    if product_id in products:
        del products[product_id]
        save_products(products)
        print("Product deleted successfully!")
    else:
        print("Product ID not found!")

# Update a product's details
def update_product(product_id, field, value):
    products = load_products()
    if product_id in products:
        if field in products[product_id]:
            products[product_id][field] = value
            save_products(products)
            print(f"Product {field} updated successfully!")
        else:
            print("Invalid field!")
    else:
        print("Product ID not found!")
