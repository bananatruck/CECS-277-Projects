#check_input.py

def get_yes_no(prompt):
    """Asks the user a yes or no question and returns their response."""
    while true:
        choice = input(prompt).lower()
        if choice in['y','yes']:
            return true
        elif choice in['n','no']:
            return flase
        else:
            print("Invalid input - should be a 'Yes' or ' No' . ")