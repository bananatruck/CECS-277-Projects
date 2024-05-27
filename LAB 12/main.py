#CECS 277 
#LAB-12
#MOHIT RAJUBHAI MORI
#In this code we followed the guidelines and instructions given by the TA and Professor.
#Tirth and Mohit, we both had given our efforts and worked on the base, concepts and designing this  lab
#We have used various concepts taught in classes like defining a function, enumerate, reading a file, caliing from other files, random, import  and so on.
#We did our test runs, and made sure the program is fail proof and handles bad input well
#We also showed the code to our TA, who gave us comments for it and helped us with an issue we faced, and hence we got the lab done perfectly.

from tasklist import Tasklist
from check_input import get_int_range

def main_menu():
    print("\n-Tasklist-")
    print(f"Tasks to complete: {len(task_list)}")
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")

    return get_int_range("Enter choice: ", 1, 6)

def get_date():
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter day: ", 1, 31)
    year = get_int_range("Enter year: ", 2000, 2100)
    return f"{month:02d}/{day:02d}/{year}"

def get_time():
    hour = get_int_range("Enter hour: ", 0, 23)
    minute = get_int_range("Enter minute: ", 0, 59)
    return f"{hour:02d}:{minute:02d}"

task_list = Tasklist()

while True:
    choice = main_menu()

    if choice == 1:
        current_task = task_list.get_current_task()
        if current_task:
            print("Current task is:")
            print(current_task)
        else:
            print("All tasks are complete.")
    elif choice == 2:
        print("Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
    elif choice == 3:
        if task_list:
            removed_task = task_list.mark_complete()
            if removed_task:
                print("Marking current task as complete:")
                print(removed_task)
                current_task = task_list.get_current_task()
                if current_task:
                    print("New current task is:")
                    print(current_task)
                else:
                    print("All tasks are complete.")
            else:
                print("All tasks are complete.")
        else:
            print("No tasks available.")
    elif choice == 4:
        task_description = input("Enter a task: ")
        print("Enter Due Date Below")
        due_date = get_date()
        print("Enter Due Time Below")
        due_time = get_time()
        task_list.add_task(task_description, due_date, due_time)
        print("-Tasklist-")
        print(f"Tasks to complete: {len(task_list)}")
        print("Task added.")
    elif choice == 5:
        print("Search by month, day, and year")
        search_date = get_date()
        found = False
        print(f"Tasks due on {search_date}:")
        for task in task_list:
            if task.date == search_date:
                print(task)
                found = True
        if not found:
            print("No tasks found for the given date.")
    elif choice == 6:
        task_list.save_file()
        print("Saving List...")
        break