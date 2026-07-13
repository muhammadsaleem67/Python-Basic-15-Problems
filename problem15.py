"""*15. Simple To-Do List*  
Make a mini program with a menu:  
1. Add task  
2. View tasks  
3. Exit  
Store tasks in a list and loop until the user exits."""
while True :
    print("""Make a mini program with a menu:
1. Add task  
2. View tasks  
3. Exit  
Store tasks in a list and loop until the user exits.""")
        
    choice = int(input("Enter a choice : "))
    if choice == 1:
        print("Add task")   
        tasks = []
        task = int(input("How much tasks you want to add : "))
        for i in range(0, task):
            tasks.append(input("Enter task : "))     
    
    elif choice == 2 :
        print("Your tasks")
        print(tasks)
    elif choice == 3 :
        print("You exited")
    else : 
        print("Invalid Choice")

    if choice == 3 :
        break

    
    
