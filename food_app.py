from food_item import FoodItem
from user_app import User

class FoodOrderingApp:
    def __init__(self):
        self.food_items = []
        self.users = []
        self.current_user = None
        self.order_history = []



    def login_user(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                print("Login successful!")
                return
        print("Invalid email or password!")

    def register_user(self):
        full_name = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)
        print("Registration successful!")

    def add_food_item(self):
        name = input("Enter the food item name: ")
        quantity = input("Enter the quantity: ")
        price = float(input("Enter the price: "))
        discount = float(input("Enter the discount: "))
        stock = int(input("Enter the stock: "))
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")

    def edit_food_item(self):
        food_id = int(input("Enter the FoodID of the item to edit: "))
        name = input("Enter the new name: ")
        quantity = input("Enter the new quantity: ")
        price = float(input("Enter the new price: "))
        discount = float(input("Enter the new discount: "))
        stock = int(input("Enter the new stock: "))
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully!")
                return
        print("Food item not found!")

    def view_food_item(self):
        print("Food Items:")
        for food_item in self.food_items:
            print(f"ID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, "
                  f"Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")

    def remove_food_item(self):
        food_id = int(input("Enter the FoodID of the item to remove: "))
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                return
        print("Food item not found!")

    def place_new_order(self):
        print("Available Food Items:")
        for food_item in self.food_items:
            print(f"{food_item.food_id}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}]")
        selected_items = input("Enter the numbers of the items you want to order (separated by commas): ")
        selected_items = [int(item) for item in selected_items.split(",")]
        self.place_order(selected_items)

    def place_order(self, selected_items):
        if not selected_items:
            print("No items selected!")
            return

        order_items = []
        total_price = 0
        for food_id in selected_items:
            for food_item in self.food_items:
                if food_item.food_id == food_id:
                    order_items.append(food_item)
                    total_price += food_item.price
                    break

        if not order_items:
            print("No valid items selected!")
            return

        self.order_history.append((self.current_user, order_items, total_price))
        print("Order placed successfully!")
        print("Ordered Items:")
        for food_item in order_items:
            print(f"Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}")
        print(f"Total Price: {total_price}")

    def view_order_history(self):
        if not self.order_history:
            print("No order history!")
            return

        print("Order History:")
        for order in self.order_history:
            user = order[0]
            order_items = order[1]
            total_price = order[2]

            print(f"User: {user.full_name}, Total Price: {total_price}")
            print("Ordered Items:")
            for food_item in order_items:
                print(f"Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}")

    def update_profile(self):
        if self.current_user is None:
            print("You are not logged in!")
        else:

            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            address = input("Enter your address: ")
            password = input("Enter your new password: ")
            self.current_user.full_name = full_name
            self.current_user.phone_number = phone_number
            self.current_user.address = address
            self.current_user.password = password
            print("Profile updated successfully!")
