# check_input.py

def get_yes_no(prompt):
    """Asks the user a yes or no question and returns their response."""
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid input - should be a 'Yes' or 'No'.")
