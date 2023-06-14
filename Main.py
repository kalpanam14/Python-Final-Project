from food_app import FoodOrderingApp

class Main:
    def execute(self, choice, food):
        if choice == 1:
            print("******************Login User ********************")
            food.login_user()
        if choice == 2:
            print("*******************eUser Registration********************")
            food.register_user()
        if choice == 3:
            print("***********************Add food item *****************")
            food.add_food_item()
        if choice == 4:
            print("**************************** Edit food item*****************")
            food.edit_food_item()
        if choice == 5:
            print("****************************View Food Add item *************")
            food.view_food_item()
        if choice == 6:
            print("************************* Remove Food Item *************")
            food.remove_food_item()
        if choice == 7:
            print("*****************************Place New Order ****************")
            food.place_new_order()
        if choice == 8:
            print("********************************View Orde Historyr********************")
            food.view_order_history()
        if choice == 9:
            print("********************************* Update profile************************")
            food.update_profile()
if __name__ == "__main__":

    food = FoodOrderingApp()

    main = Main()

    while True:
        choice = int(input("Enter \n 1.Login user \n 2. EUser Registration\n 3. Add Food Item \n 4. Edit Food Item  \n 5. View Food Item  \n 6. Delete Food Item \n 7. Place New Order \n 8. View Order history \n 9. Update Profile \n"))
        main.execute(choice, food)
