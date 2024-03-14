#=====importing libraries===========
import os
import getpass
from datetime import datetime, date
from tabulate import tabulate

# Skills Bootcamp in Software Engineering (Fundamentals)
# Task 17 - Capstone Project - Lists, Functions, and String Handling
# 10-025-1 Capstone Project - Lists, Functions and String Handling
# Capstone Project Task 1
# task_manager.py
# 19-Feb-2024 V1

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# text color 
class Color:
    COLORS = {
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'DARKCYAN': '\033[36m',
        'BLUE': '\033[94m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'CYAN_BOLD_ITALIC': '\x1b[;36;1;3m',
        'END': '\033[0m'
    }

    @classmethod
    def decorate(cls, text, color):
        color_code = cls.COLORS.get(color.upper())
        if color_code:
            return f"{color_code}{text}{cls.COLORS['END']}"
        else:
            return text
        
    # color headprint cyan 
    @classmethod
    def headerprintcyan(cls, text, padding=50):
        padded_text = text.ljust(padding)
        return f"\033[1;44m {padded_text} \033[m"
    
    # Pink header data can be changed
    @classmethod
    def headerprintred(cls, text, padding=50):
        padded_text = text.ljust(padding)
        return f"\x1b[45m {padded_text} \x1b[m"


# read the file the last modiify data & time 
def get_last_update_time(file_path):
    if os.path.exists(file_path):
        # Get the last modification time of the file in seconds since the epoch
        last_update_timestamp = os.path.getmtime(file_path)
        
        # Convert the timestamp to a datetime object
        last_update_datetime = datetime.fromtimestamp(last_update_timestamp)
        return last_update_datetime
    else:
        print(f"File '{file_path}' not found.")
        return None


# Define Minimum password fuction 
def IsValidPassword(new_password):   
    length = lower = upper = digit = False
    if len(new_password)>= 8:
        length = True   
        for letter in new_password:
            if letter.islower():
                lower = True
            elif letter.isupper():
                upper = True
            elif letter in "0123456789":
                digit = True
    return length and lower and upper and digit

# Define function to validate task_title input
def validate_task_title(task_title):
    return task_title in ["1", "2", "3", "4","5","6", "7", "8", "9","10","11","12"]


# Define tasks mapping full name
def task_map_name(task_title):

    TaskMapName = {
        "1": "Coding",
        "2": "Code Review",
        "3": "Design",
        "4": "Testing",
        "5": "Collabortation",
        "6": "Problem Solving",
        "7": "Research",
        "8": "Documentation",
        "9": "Deployment",
        "10": "Maintenance",
        "11": "Add functionality to task manager",
        "12": "Other"
    }
    # Get the title name based on the selected task_title
    TaskMapName = TaskMapName.get(task_title, 0)
    return TaskMapName


# Display Wecome pages
def welcomepage():
    print(Color.decorate(r"Welcome. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 'CYAN'))
    print(Color.decorate(r"                                                                    ", 'CYAN'))
    print(Color.decorate(r"   _______        _      __  __                                     ", 'CYAN'))
    print(Color.decorate(r"  |__   __|      | |    |  \/  |                                    ", 'CYAN'))
    print(Color.decorate(r"     | | __ _ ___| | __ | \  / | __ _ _ __   __ _  __ _  ___ _ __   ", 'CYAN'))
    print(Color.decorate(r"     | |/ _` / __| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|  ", 'CYAN'))
    print(Color.decorate(r"     | | (_| \__ \   <  | |  | | (_| | | | | (_| | (_| |  __/ |     ", 'GREEN'))
    print(Color.decorate(r"     |_|\__,_|___/_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|     ", 'GREEN'))
    print(Color.decorate(r"                                                   __/ |            ", 'GREEN'))
    print(Color.decorate(r"                                                  |___/             ", 'GREEN'))
    print(Color.decorate(r"                                                             SYSTEM ", 'GREEN'))
    print(Color.decorate(r". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . .", 'GREEN'))


# Function to load task data from tasks.txt file
def load_tasks():
    """Load task data from tasks.txt file."""
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass

    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    task_list = []

    # Convert task data strings into dictionaries and append to task_list
    for t_str in task_data:
        curr_t = {}
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)
    return task_list


# Function to load user data from user.txt file
def load_users():
    """Load user data from user.txt file."""
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    return username_password

# Function for user login
def login(username_password):
    """Prompt user for login credentials."""
    logged_in = False
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = getpass.getpass("Password: ")
        if curr_user not in username_password.keys():
            print(Color.decorate('User does not exist.', 'PURPLE'))
            continue
        elif username_password[curr_user] != curr_pass:
            print(Color.decorate('Wrong password', 'PURPLE'))
            continue
        else:
            print("Login Successful!")
            logged_in = True
            return curr_user


# Define 'r'-Registering a User
def reg_user(username_password, curr_user):
    """Add a new user to the user.txt file."""
    if curr_user == 'admin':
        new_username = input("New Username (at least 3 characters): ")
        while not int(len(new_username))>=3:
            print(Color.decorate('Username must be at least 3 characters long. Please try again.', 'PURPLE'))
            new_username = input("New Username (at least 3 characters): ")
            break

        while new_username in username_password:
                print(Color.decorate(f"Username '{new_username}' already exists. Please choose another username.\n"
                    "To change your password, please return to the menu\n"
                    "and select 'c' for Change Password.", 'PURPLE'))
                return  # Exit the function if username already exists
        

        user_password = input("Enter new password: ")
        is_valid = IsValidPassword(user_password)
        if is_valid:
            # Proceed with password change
            confirm_password = input("Confirm new password: ")
            if user_password == confirm_password:
                print(Color.decorate(f"New user added", 'CYAN'))
                username_password[new_username] = user_password
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
            else:
                print(Color.decorate('User Password do not match confrim Password.', 'PURPLE'))
        else:
            print(Color.decorate('Invalid password. Please try again.', 'PURPLE'))
            print(Color.decorate('Password must meet the following requirements:', 'DARKCYAN'))
            print(Color.decorate("""
                    1. The password must be at least eight characters long.
                    2. It must contain at least one uppercase letter.
                    3. It must contain at least one lowercase letter.
                    4. It must contain at least one numeric digit.             
                    """,'GREEN'))
    else:
        print(Color.decorate('Only admins can register new users.', 'PURPLE'))


# Define Change password function
def change_password(username_password, curr_user):
    new_password = input("Enter new password: ")
    is_valid = IsValidPassword(new_password)
    if is_valid:
        # Proceed with password change
        confirm_password = input("Confirm new password: ")

        if new_password == confirm_password:
                # Check if the current user is an admin
                if curr_user == 'admin':
                    user_to_change = input("Enter the username whose password you want to change: ")
                    if user_to_change in username_password:
                        username_password[user_to_change] = new_password
                        with open("user.txt", "w") as out_file:
                            user_data = []
                            for k in username_password:
                                user_data.append(f"{k};{username_password[k]}")
                            out_file.write("\n".join(user_data))
                        print(Color.decorate(f"Password for user '{user_to_change}' changed successfully.", 'CYAN'))
                    else:
                        print(Color.decorate('User does not exist.', 'PURPLE'))
                else:
                    # Non-admin users can only change their own password
                    username_password[curr_user] = new_password
                    with open("user.txt", "w") as out_file:
                        user_data = []
                        for k in username_password:
                            user_data.append(f"{k};{username_password[k]}")
                        out_file.write("\n".join(user_data))
                    print("Password changed successfully.")
        else:
                 print(Color.decorate('Passwords do not match. Please try again.', 'PURPLE')) 
    else:
        print(Color.decorate('Invalid password. Please try again.', 'PURPLE'))
        print(Color.decorate('Password must meet the following requirements:', 'DARKCYAN'))
        print(Color.decorate("""
                1. The password must be at least eight characters long.
                2. It must contain at least one uppercase letter.
                3. It must contain at least one lowercase letter.
                4. It must contain at least one numeric digit.             
                """,'GREEN'))


# Function to add a new task
def add_task(task_list, username_password,curr_user):
    """Allow a user to add a new task to task.txt file."""

    if curr_user == 'admin':
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print(Color.decorate('User does not exist. Please enter a valid username', 'PURPLE'))
            return
        
        print('''
            1.Coding,
            2.Code Review,
            3.Design,
            4.Testing,
            5.Collabortation,
            6.Problem Solving,
            7.Research,
            8.Documentation,
            9.Deployment,
            10.Maintenance,
            11.Add functionality to task manager
            12.Other
            ''')
        # Get user inputs for city_flight and validate
        task_title = input("Enter the number corresponding to the title of the task. : ")
        while not validate_task_title(task_title):
            print(Color.decorate("Error: Please enter a valid the number corresponding to the title of the task."  ,'PURPLE'))
            task_title = input("Enter the number corresponding to the title of the task. : ")
        task_tile = task_map_name(task_title)

        #task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print(Color.decorate('Invalid datetime format. Please use the format specified', 'PURPLE'))

        curr_date = date.today()

        new_task = {
            "username": task_username,
            "title": task_map_name(task_title),
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


# Function to view all tasks
def view_all(task_list):
    """Read tasks from tasks.txt file and print to the console."""
    from tabulate import tabulate
    
    # Initialize a list to hold the data for tabulate
    table_data = []
    
    for t in task_list:
        task_info = [
            t['title'],
            t['description'],
            t['username'],
            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            t['due_date'].strftime(DATETIME_STRING_FORMAT)
        ]
        table_data.append(task_info)

    print(Color.decorate('All tasks source from tasks.txt file', 'CYAN_BOLD_ITALIC'))
    # Define table headers
    headers = ["Task", "Description", "Assigned to", "Date Assigned", "Due Date"]

    # Generate tabulate report
    report = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
    print(report)


# Function to view tasks assigned to the current user
def view_mine(task_list,username_password, curr_user):
    """Read tasks from tasks.txt file assigned to the current user."""

    print(Color.decorate(f"Viewing tasks assigned to {curr_user}:", 'CYAN_BOLD_ITALIC'))
    print()
    tasks_assigned_to_user = [t for t in task_list if t['username'] == curr_user]

    if not tasks_assigned_to_user:
        print(Color.decorate('No tasks assigned to current user.', 'CYAN'))
        return

    from tabulate import tabulate

    # Initialize a list to hold the data for tabulate
    table_data = []

    for i, t in enumerate(tasks_assigned_to_user, 1):
        task_info = [
            f"{i}. {t['title']}",
            t['description'],
            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            t['due_date'].strftime(DATETIME_STRING_FORMAT),           
            "Yes" if t['completed'] else "No"  # Include Completed status
        ]
        table_data.append(task_info)
    # tablefmt="grid" tablefmt="fancy_outline"
    print(tabulate(table_data, headers=["Task", "Description", "Date Assigned", "Due Date", "Completed"], tablefmt="grid"))
    print()
    while True:
        choice = input("Enter the number of the task you want to select (or -1 to return to the main menu): ")
        print()
        if choice == '-1':
            return  # Return to the main menu
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tasks_assigned_to_user):
                selected_task = tasks_assigned_to_user[index]
                print(Color.decorate('Please check the selected items：', 'CYAN_BOLD_ITALIC'))
                table = [
                        ["Task : ", selected_task['title']],
                        ["Description : ", selected_task['description']],
                        ["Task assigned : ", selected_task['username']],
                        ["assigned_date] : ",selected_task['assigned_date']]
                    ]

                print(tabulate(table, headers=["Selected Task", "Content"], tablefmt="grid"))

                action = input("Select action (c: mark as complete, e: edit task, -1: return to main menu): ")
                if action == 'c':
                    if not selected_task['completed']:
                        selected_task['completed'] = True
                        print("Task marked as complete.")
                        # Update task status in the main task list
                        for task in task_list:
                            if (task['title'] == selected_task['title'] and 
                                task['username'] == selected_task['username'] and 
                                task['description'] == selected_task['description']):
                                task['completed'] = True
                                break

                    else:
                        print("Task is already marked as complete.")
                elif action == 'e':
                    if not selected_task['completed']:
                        edit_option = input("Select option to edit (u: username, d: due date, -1: return to main menu): ")
                        if edit_option == 'u':
                            new_username = input("Enter new username: ")

                            if new_username not in username_password.keys():
                                print(Color.decorate('User does not exist.', 'PURPLE'))
                                continue
                            else:
                                selected_task['username'] = new_username
                                print("Username updated successfully.")

                        elif edit_option == 'd':
                            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                            try:
                                selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                print("Due date updated successfully.")
                            except ValueError:
                                print(Color.decorate('Invalid date format. Please use the format YYYY-MM-DD.', 'PURPLE'))
                        elif edit_option == '-1':
                            continue  # Continue loop to return to the main menu
                        else:
                            print(Color.decorate('Invalid option. Please try again', 'PURPLE'))
                    else:
                        print(Color.decorate('Task cannot be edited as it is already marked as complete.', 'PURPLE'))
                elif action == '-1':
                    return  # Return to the main menu
                else:
                    print(Color.decorate('Invalid action. Please try again', 'PURPLE'))
            else:
                print(Color.decorate('Invalid task number. Please try again.', 'PURPLE'))
        else:
            print(Color.decorate('Invalid input. Please enter a number', 'PURPLE'))


# Function to generate task overview report
def generate_task_overview(task_list):
    #Generate task overview report.
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'] < datetime.today())

    total_incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    data = [
        ["Total tasks", total_tasks],
        ["Completed tasks", completed_tasks],
        ["Uncompleted tasks", uncompleted_tasks],
        ["Overdue tasks", overdue_tasks],
        ["Percentage of incomplete tasks", f"{total_incomplete_percentage:.2f}%"],
        ["Percentage of overdue tasks", f"{overdue_percentage:.2f}%"]
    ]

    headers = ["Metric", "Value"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    table_print = tabulate(data, headers=headers, tablefmt="grid")

    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("Task Overview Report\n")
        task_overview_file.write(table)

 
# Function to generate user overview report
def generate_user_overview(task_list, username_password):
    """Generate user overview report."""
    total_users = len(username_password)
    total_tasks = len(task_list)

    user_task_counts = {username: 0 for username in username_password}
    user_completed_counts = {username: 0 for username in username_password}
    user_overdue_counts = {username: 0 for username in username_password}

    for task in task_list:
        user_task_counts[task['username']] += 1
        if task['completed']:
            user_completed_counts[task['username']] += 1
        elif task['due_date'] < datetime.today():
            user_overdue_counts[task['username']] += 1

    data = []
    for username in username_password:
        user_total_tasks_percentage = (user_task_counts[username] / total_tasks) * 100 if total_tasks > 0 else 0
        user_completed_percentage = (user_completed_counts[username] / user_task_counts[username]) * 100 if user_task_counts[username] > 0 else 0
        user_uncompleted_percentage = 100 - user_completed_percentage
        user_overdue_percentage = (user_overdue_counts[username] / user_task_counts[username]) * 100 if user_task_counts[username] > 0 else 0

        data.append([
            username,
            user_task_counts[username],
            f"{user_total_tasks_percentage:.2f}%",
            f"{user_completed_percentage:.2f}%",
            f"{user_uncompleted_percentage:.2f}%",
            f"{user_overdue_percentage:.2f}%"
        ])

    headers = ["Username", "Total Tasks", "Total Tasks (%)", "Completed Tasks (%)", "Uncompleted Tasks (%)", "Overdue Tasks (%)"]
    table = tabulate(data, headers=headers, tablefmt="grid")

    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write("User Overview Report\n")
        user_overview_file.write(table)

# Define function print file time
def display_report_file_time():
 
    # print USER Statistics Report from user_overview.txt
    print(Color.decorate('Generate Real-time Reporting ', 'CYAN_BOLD_ITALIC'))
    print()
    print(Color.decorate(' Read the text file User Overview Report ', 'BLUE'))
    file_path2 = "user_overview.txt"
    last_update_time2 = get_last_update_time(file_path2)

    if last_update_time2:
        print(f"The last update time of '{file_path2}' was: {last_update_time2}")

    with open('user_overview.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines() 

    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        print("{}".format(line.strip()))

    # print TASK Statistics Report from task_overview.txt
    print()
    print(Color.decorate(' Read the text file Tasks Overview Report ', 'BLUE'))
    file_path = "task_overview.txt"
    last_update_time = get_last_update_time(file_path)

    if last_update_time:
        print(f"The last update time of '{file_path}' was: {last_update_time}")
    with open('task_overview.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines() 

    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        print("{}".format(line.strip()))

def display_statistics(task_list, username_password,curr_user):
    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    table = [
        ["Number of users :", num_users],
        ["Number of tasks :", num_tasks]
    ]

    print(Color.decorate('Display Statistics Report', 'BLUE'))
    print(tabulate(table, headers=["Items List", "Total(sum)"], tablefmt="fancy_outline"))

    # print USER Statistics Report from user_overview.txt
    print()
    print(Color.decorate('User Statistics Report', 'BLUE'))
    
    filename = 'user_overview.txt'
    if os.path.exists(filename):
        # with open('user_overview.txt', 'r', encoding='utf-8') as file:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()         


        count = 0
        # Strips the newline character
        for line in lines:
            count += 1
            print("{}".format(line.strip()))
        
    else:
        print(f"File '{filename}' no data generated.")

    # print TASK Statistics Report from task_overview.txt
    print()
    print(Color.decorate('Task Statistics Report', 'BLUE'))
    
    filename = 'task_overview.txt'
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines() 

        count = 0
        # Strips the newline character
        for line in lines:
            count += 1
            print("{}".format(line.strip()))
            
    else:
        print(f"File '{filename}' no data generated.")


# Main function to run the task manager
def main():
    """Main function to run the task manager."""
    # Call display welcomepage
    welcomepage()
    task_list = load_tasks()
    username_password = load_users()
    curr_user = login(username_password)

    while True:
        print()

        if curr_user == "admin":
            menu = input('''Select one of the following Options below:
            r  - Registering a User
            a  - Adding a Task
            va - View All Tasks
            vm - View My Tasks
            gr - Generate Report
            ds - Display Statistics
            c  - Change Password
            e  - Exit
            : ''').lower()  # Convert input to lowercase   
        else:
            menu = input('''Select one of the following Options below:
            va - View All Tasks
            vm - View My Tasks
            c  - Change Password
            e  - Exit
            : ''').lower()

        if menu == 'r':
            print(Color.headerprintred("Registering a User"))
            print()
            reg_user(username_password, curr_user)

        elif menu == 'a':
            print(Color.headerprintred("Adding a Task"))
            print()
            add_task(task_list, username_password,curr_user)

        elif menu == 'va':
            print(Color.headerprintcyan("View All Tasks"))
            print()
            view_all(task_list)

        elif menu == 'vm':
            print(Color.headerprintred("View My Tasks"))
            print()
            view_mine(task_list, username_password, curr_user)

        elif menu == 'gr':
            print(Color.headerprintcyan("Generate Report"))
            print()
            generate_task_overview(task_list)
            generate_user_overview(task_list, username_password)
            display_report_file_time()

        elif menu == 'ds' and curr_user == 'admin': 
            print(Color.headerprintcyan("Display Statistics"))
            print()
            display_statistics(task_list, username_password,curr_user)
            
        elif menu == 'c':
            print(Color.headerprintred("Chagne Password"))
            print()
            change_password(username_password, curr_user)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print(Color.decorate('You have made a wrong choice, Please Try again', 'PURPLE'))

if __name__ == "__main__":
    main()


