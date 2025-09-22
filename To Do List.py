#Simple To Do list

def menu():
    #displays the menu for the user
    print("\n --- Menu ---")
    print("1. New Task")
    print("2. Current Tasks")
    print("3. Mark Complete Task")
    print("4. Remove Task")
    print("5. Exit")

def add_task(tasks, task_id_counter):
    #Allows the addition of a new task
    task_name = input("Enter the new task: ")
    tasks[task_id_counter] = {"name": task_name, "complete" : False}
    print(f"Task ' {task_name}' added.")
    return task_id_counter + 1

def view_tasks(tasks):
    #displays all tasks and status
    if not tasks:
        print(" No Tasks on the list.")
        return

    print("\n--- Your To Do list ---")
    for task_id, task_info in tasks.items():
        status = "(DONE)" if task_info["complete"] else "(DO)"
        print(f"[{task_id}] {status} {task_info['name']}")

def mark_complete(tasks):
        #marks a task complete based on ID
        view_tasks(tasks)
        try:
            task_id = int(input("Enter the ID of the task to mark complete: "))
            if task_id in tasks:
                tasks[task_id]["complete"] = True
                print(f"Task '{tasks[task_id]['name']}' marked as complete.")
            
            else:
                print("Error: Task ID not found.")
        except ValueError:
            print("Invalid Input. Enter a Number.")

def remove_task(tasks):
        #removes task based on ID
        view_tasks(tasks)
        try:
            task_id = int(input("Enter the ID of task to remove: "))
            if task_id in tasks:
                removed_task = tasks.pop(task_id)
                print(f"Task' {removed_task['name']} ' removed.")
            else:
                print("Error: Task ID not found.")
        except ValueError:
            print("Invalid input. Enter a number.")


def main():
    #Main function to run program
    tasks = {}
    task_id_counter = 1

    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_id_counter = add_task(tasks, task_id_counter)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()