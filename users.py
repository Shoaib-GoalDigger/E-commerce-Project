# users.py
import json

# File to store user data
USER_FILE = "users.json"  # Use consistent naming conventions (UPPERCASE for constants)

# Load users from file
def load_users():
    try:
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Fixed: Return an empty dictionary if the file doesn't exist

# Save users to file
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Add a new user
def add_user(user_id, name, email):  # Corrected argument order for consistency
    users = load_users()
    if user_id in users:
        print("User ID already exists!")
    else:
        users[user_id] = {"name": name, "email": email}
        save_users(users)
        print("User added successfully!")

# View all users
def view_users():
    users = load_users()  # Fixed: Added parentheses to call the function
    if not users:
        print("No users found!")
    else:
        for user_id, details in users.items():  # Fixed: Changed `item()` to `items()`
            print(f"ID: {user_id}, Name: {details['name']}, Email: {details['email']}")

# Delete a user
def delete_user(user_id):
    users = load_users()
    if user_id in users:
        del users[user_id]
        save_users(users)
        print("Deleted successfully!")
    else:
        print("User ID not found!")

