from database import get_connection
from classes.user import User
from classes.item import Item
from classes.bid import Bid

def main():
    ADMIN_USERNAME = "chinara"
    ADMIN_PASSWORD = "2003"

    # Establish database connection
    conn = get_connection()

    if conn:
        try:
            cursor = conn.cursor()

            while True:
                print("\n=== Main Menu ===")
                print("1. Admin Login")
                print("2. User Login")
                print("3. Register")
                print("4. Exit")

                choice = input("Enter your choice (1-4): ")

                if choice == '1':
                    admin_username = input("Enter admin username: ")
                    admin_password = input("Enter admin password: ")
                    if admin_username == ADMIN_USERNAME and admin_password == ADMIN_PASSWORD:
                        admin_menu(cursor)
                    else:
                        print("Invalid admin username or password. Please try again.")

                elif choice == '2':
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    user = User.login(cursor, username, password)
                    if user:
                        user_menu(cursor, user)
                    else:
                        print("Invalid username or password. Please try again.")

                elif choice == '3':
                    register(cursor)

                elif choice == '4':
                    break

                else:
                    print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the database connection
            conn.close()

    else:
        print("Failed to connect to the database.")

def admin_menu(cursor):
    print("\n=== Admin Menu ===")
    print("1. View All Items")
    print("2. Delete Item")
    print("3. Exit")
    admin_choice = input("Enter your choice (1-3): ")

    if admin_choice == '1':
        items = Item.get_all_items(cursor)
        print("\nAll items:")
        for item in items:
            print(item)

    elif admin_choice == '2':
        item_id = int(input("Enter the ID of the item to delete: "))
        Item.delete(cursor, item_id)
        print("Item deleted successfully.")

    elif admin_choice == '3':
        pass

    else:
        print("Invalid choice. Please try again.")

def user_menu(cursor, user):
    print("\n=== User Menu ===")
    print("1. Add Item")
    print("2. Place Bid")
    print("3. Exit")
    user_choice = input("Enter your choice (1-3): ")

    if user_choice == '1':
        item_name = input("Enter item name: ")
        description = input("Enter description: ")
        start_price = float(input("Enter start price: "))
        start_datetime = input("Enter start datetime (YYYY-MM-DD HH:MM:SS): ")
        end_datetime = input("Enter end datetime (YYYY-MM-DD HH:MM:SS): ")
        Item.add(cursor, user.user_id, item_name, description, start_price, start_datetime, end_datetime)
        print("Item added successfully.")

    elif user_choice == '2':
        item_id = int(input("Enter item ID: "))
        bid_amount = float(input("Enter bid amount: "))
        bid_datetime = input("Enter bid datetime (YYYY-MM-DD HH:MM:SS): ")
        Bid.add(cursor, item_id, user.user_id, bid_amount, bid_datetime)
        print("Bid placed successfully.")

    elif user_choice == '3':
        pass

    else:
        print("Invalid choice. Please try again.")

def register(cursor):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    User.add(cursor, username, password, email)
    print("Registration successful.")

if __name__ == "__main__":
    main()



