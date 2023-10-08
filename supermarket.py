shopping_list = []

def display_list():
    print("\nCurrent Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")


def add_item():
    item = input("\nEnter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")


def delete_item():
    display_list()
    if shopping_list:
        try:
            item_index = int(input("\nEnter the number of the item you want to delete: ")) - 1
            if 0 <= item_index < len(shopping_list):
                deleted_item = shopping_list.pop(item_index)
                print(f"{deleted_item} has been removed from your shopping list.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    else:
        print("Your shopping list is empty.")

while True:
    print("\nSupermarket Shopping List")
    print("1. Display Shopping List")
    print("2. Add Item to Shopping List")
    print("3. Delete Item from Shopping List")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        display_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        print("Thank you for using the supermarket system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")