shopping_list = []

def add_item(item):
    """
    Add an item to the shopping list.
    """
    shopping_list.append(item)
    print(f'Added "{item}" to the shopping list.')

def remove_item(item):
    """
    Remove an item from the shopping list.
    """
    try:
        shopping_list.remove(item)
        print(f'Removed "{item}" from the shopping list.')
    except ValueError:
        print(f'Item "{item}" not found in the shopping list.')

def view_list():
    """
    View all items in the shopping list.
    """
    if shopping_list:
        print("Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("The shopping list is empty.")

def exit_program():
    """
    Exit the shopping list manager.
    """
    print("Exiting the shopping list manager. Goodbye!")


def display_menu():
    print("Shopping List Manager")
    
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)

        elif choice == '2':
            item = input("Enter item to remove: ")
            remove_item(item)

        elif choice == '3':
            view_list()

        elif choice == '4':
            exit_program()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
