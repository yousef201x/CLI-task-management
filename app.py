import logic.logic as app

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def display_tasks(tasks):
    if not tasks:
        print(f"{RED}No tasks found.{RESET}")
        return

    cnt = 1
    for task in tasks:
        print(f"{BLUE}Task {cnt}:{RESET}")
        print(f"  {YELLOW}ID:{RESET} {task[0]}")
        print(f"  {YELLOW}Description:{RESET} {task[1]}")
        print(f"  {YELLOW}Due Date:{RESET} {task[2]}\n")
        cnt += 1

def colored_input(prompt, color=RESET):
    return input(f"{color}{prompt}{RESET}")

while True:
    print(f'''
    {GREEN}1- My Tasks
    2- Search Task
    3- Create Task
    4- Update Task
    5- Delete Task
    6- Exit{RESET}
    ''')

    action_input = colored_input("Enter choice: ", BLUE)

    if action_input == "1":
        choice = colored_input('''
        1- Pending Tasks
        2- Completed Tasks
        Enter choice: 
        ''', GREEN)
        if choice == "1":
            tasks = app.myTasks('pending')
            display_tasks(tasks)
        elif choice == "2":
            tasks = app.myTasks('completed')
            display_tasks(tasks)

    elif action_input == "2":
        search_term = colored_input("Enter search term: ", BLUE)
        tasks = app.searchTask(search_term)
        display_tasks(tasks)

    elif action_input == "3":
        description = colored_input("Enter task description: ", BLUE)
        due_date = colored_input("Enter due date: ", BLUE)
        status = colored_input("Enter status (optional, press Enter to default to 'pending'): ", BLUE) or 'pending'
        app.createTask(description, due_date, status)

    elif action_input == "4":
        task_id = colored_input("Enter task id: ", BLUE)
        choice = colored_input('''
        1- Update description
        2- Update due date
        3- Update status
        Enter choice: 
        ''', GREEN)

        if choice == "1":
            new_description = colored_input("Enter new description: ", BLUE)
            app.updateTask(taskID=task_id, description=new_description)
        elif choice == "2":
            new_date = colored_input("Enter new due date: ", BLUE)
            app.updateTask(taskID=task_id, date=new_date)
        elif choice == "3":
            new_status = colored_input("Enter new status: ", BLUE)
            app.updateTask(taskID=task_id, status=new_status)

    elif action_input == "5":
        task_id = colored_input("Enter task ID to delete: ", BLUE)
        app.deleteTask(task_id)

    elif action_input == "6":
        print(f"{RED}Exiting...{RESET}")
        break

    else:
        print(f"{RED}Invalid input, please try again.{RESET}")
