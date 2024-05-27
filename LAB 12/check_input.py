def get_int_range(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Input must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input; please enter an integer.")