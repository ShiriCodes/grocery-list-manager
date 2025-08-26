"""
Grocery List Manager

This program allows a user to manage a grocery list via a menu interface.
The user can:
- Print the list of items
- Count items in the list
- Check if an item exists
- Count occurrences of an item
- Add or remove an item
- Identify invalid items (less than 3 characters or containing non-letter characters)
- Remove duplicates
- Exit the program

The program reads a single comma-separated input string from the user to initialize
the grocery list. Menu choices are entered as integers (1-9).

GitHub: ShiriCodes
Date: 2025-08-26
"""

def input_validator(basic_service_input):
    """Validate menu input and return it as an integer (1-9)."""
    if not basic_service_input.isdigit():
        raise TypeError ("Input must be an integer.")
    chosen_service = int(basic_service_input)
    if chosen_service < 1 or chosen_service > 9:
        raise ValueError ("Input must be an integer in the range 1-9")
    return chosen_service

def case_desensitize(my_data: list[str] | str):
    """Return lowercase version of a string or list of strings."""
    if isinstance(my_data, list) and all(isinstance(item, str) for item in my_data):
        return [item.casefold() for item in my_data]
    elif isinstance(my_data, str):
        return my_data.casefold()
    else:
        raise TypeError ("This function accepts arguments of list[str] or str type only.")

def is_on_list(my_list: list[str], item: str):
    """Returns true/false based on whether item is on list."""
    item = case_desensitize(item)
    my_list = case_desensitize(my_list)
    return item in my_list

def item_counter(my_list: list[str], item: str):
    """Returns number of repeats of an item on list."""
    item = case_desensitize(item)
    my_list = case_desensitize(my_list)
    return my_list.count(item)

def list_editor(my_list: list[str], action: str, item: str):
    """Add or remove an item from the list (case-insensitive)."""
    item = case_desensitize(item)
    if action == 'add':
        my_list.append(item)
        return True
    elif action == 'remove':
        for i, existing_item in enumerate(my_list):
            if case_desensitize(existing_item) == item:
                del my_list[i]
                return True
        return False
    else:
        raise ValueError(f"Unknown action: {action}")

def find_invalid_items(my_list: list[str]):
    """Returns list of invalid items on original list (containing less than 3 characters or non-letter characters)."""
    invalid_item_list = []
    for item in my_list:
        if len(item) < 3:
            invalid_item_list.append(item)
        elif not item.isalpha():
            invalid_item_list.append(item)
    return invalid_item_list

def unique_maker(my_list: list[str]):
    """Remove duplicates from the list (case-insensitive) and modify the original list."""
    unique_items = []
    seen = set()
    for item in my_list:
        if item.casefold() not in seen:
            seen.add(item.casefold())
            unique_items.append(item)
    if len(unique_items) == len(my_list):
        return False
    else:
        my_list[:] = unique_items
        return True

def list_check(my_list: list[str]):
    """Returns true if there are items on the list, false if empty."""
    return len(my_list) > 0

def list_print(my_list: list[str]):
    """Prints list or message about list being empty after checking list is not empty."""
    if list_check(my_list) is True:
        print("\nYour current list is:\n", " ".join(my_list), "\n")
    else:
        print("\nYour list is currently empty.\n")

def menu_input():
    """Prompt the user to select a menu option and validate the input."""
    basic_service_input = input(menu)
    return input_validator(basic_service_input)

def menu_options(my_list: list[str], chosen_service: int) :
    """Execute the menu option corresponding to the chosen service."""
    if chosen_service == 1:
        list_print(my_list)
    elif chosen_service == 2:
        print("Number of items in your list: \n", len(my_list),"\n")
    elif chosen_service == 3:
        item = input("Please enter the item you would like to check: ")
        if is_on_list(my_list, item) is True:
            print("This item is on your list.\n")
        else:
            print("This item is not on your list.\n")
    elif chosen_service == 4:
        item = input("Please enter the item you would like to count: ")
        count = item_counter(my_list, item)
        if count == 0:
            print("There are no such items on your current list.\n")
        elif count == 1:
                print("This item appears once on your list.\n")
        else:
            print("This item appears ",count, " times on your list.\n")
    elif chosen_service == 5:
        item = input("Please enter the item you would like to remove from list: ")
        if list_editor(my_list, 'remove', item) is True:
            print("Item has been removed successfully.\n")
        else:
            print("Item has not been removed successfully."
            "\nCause: Item not on list.\n")
        list_print(my_list)
    elif chosen_service == 6:
        item = input("Please enter the item you would like to add to list: ")
        list_editor(my_list,'add',item)
        print("Item has been added successfully.\n")
        list_print(my_list)
    elif chosen_service == 7:
        if not list_check(find_invalid_items(my_list)):
            print("There are no invalid items on your list.\n")
        else:
            print("These are the invalid items on your list:\n", " ".join(find_invalid_items(my_list)),"\n")
    elif chosen_service == 8:
        if unique_maker(my_list) is True:
            print("Item duplicates were removed successfully.\n")
        else:
            print("There are no duplicates in your list.\n")
        list_print(my_list)
    else:
        print("\nOk. Goodbye.")
        return False
    return True

def run_menu(my_list: list[str]):
    """Run the main menu loop until the user chooses to exit."""
    while True:
        try:
            choice = menu_input()
        except (TypeError, ValueError) as e:
            print(e)
            continue
        if not menu_options(my_list, choice):
            break

groceries = [item for item in input("Enter your groceries below- "
                  "\nTry to separate items with commas - no spaces."
                  "\nFor example: 'Milk,Cottage,Tomatoes'"
                  "\nPlease enter here: ").split(',') if item]
menu = ("Service menu:"
                                    "\n1 Print list"
                                    "\n2 Check list length"
                                    "\n3 Check if item is on list"
                                    "\n4 Check number of item occurrences"
                                    "\n5 Remove item from list"
                                    "\n6 Add item to list"
                                    "\n7 Print invalid items from list"
                                    "\n8 Remove item duplicates from list"
                                    "\n9 Exit menu"
                                    "\nPlease enter your chosen service (1-9):  ")
def main():
    run_menu(groceries)

if __name__ == '__main__':
    main()