"""
To-Do List CLI Applicationreporation
A simple command-line task manager built using Python.
Features: Add, View, Delete Tasks
"""


tasks = []

while True:
    print("\n====================")
    print("      TO-DO MENU")
    print("====================")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")


    choice = input("Enter your choice : ")

    if(choice == "1"):
       task = input("Enter task: ")
       tasks.append(task)
       print("Task added successfully!")

    elif(choice == "2"):
        if len(tasks) == 0:
            print("No task available")
        else:
            print("Your task")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
    
    elif(choice == "3"):
        delete = int(input("Enter task number to delete : "))
        if 1 <= delete <= len(tasks):
            tasks.pop(delete - 1)
            print("Task deleted!")
        else:
            print("Invalid number!")

    elif(choice == "4"):
        print("GoodBye!")
        break

    else:
        print("Invalid choice!")

    