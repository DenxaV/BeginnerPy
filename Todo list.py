Tasks = []

def addTask():
    global Tasks  # 
    task = input("Please enter a task: ")
    Tasks.append(task)
    print(f"Task {task} added to the list")

def listTasks():
    global Tasks  
    if not Tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(Tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    global Tasks  
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(Tasks):
            Tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} deleted.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

if __name__ =="__main__":
    print("Your todo list: ")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("-------------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            print("Goodbye!")
            break 
        else:
            print("Invalid input.")
