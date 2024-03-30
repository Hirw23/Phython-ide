import user
import product

def main():
    print("-----------------------------------------------")
    print("WELCOME TO InnovEd MARKET - Buy && Sell Stuffs")
    print("------------------------------------------------")
    user_id = None
    while True:
        if user_id is None:
            print("1. Register\n2. Login\n3. Exit")
            choice = input("Enter your choice here: ")
            if choice == "1":
                user.register_user()
            elif choice == "3":
                break
        else:
                print("1. Add Product\n2. View All Products\n3. Logout")
                choice = input("Choose an option: ")
                if choice == "1":
                    product.add_product(user_id)
                elif choice == "2":
                    product.view_products()
                elif choice == "3":
                    user_id = None  # This logs out the user by resetting user_id to None
                    print("You have been logged out.")


if __name__ == "__main__":
    main()

