tasks = [] #empty list

def addTask(): #creating our add task function 
    task = input('Please enter a task:')
    tasks.append(task)
    print(f'Task{task} added to the list.')


def listTasks():
    if not tasks: 
        print('There are no tasks currently.')
    else: 
        print('Current Tasks:')
        for index, task in enumerate(tasks):
            print(f'Task #{index}. {task}')
            
            ### Task #1. Take out the Groceries
def deleteTask(): 
    listTasks()
    try:
        taskToDelete = int(input('Enter the # of the task you want to delete:'))
        if taskToDelete < len(tasks): 
            tasks.pop(taskToDelete)
            print(f'Task {taskToDelete} has been removed.')
        else: 
                print(f'Task #{taskToDelete} was not found.')
    except:
        print('Invalid input, please try again.')

if __name__== "__main__":
# Create a loop to run the app

#menu
    print(f'To-Do list:')

while True: 
    print('\n')
    print('Select one of the following options')
    print('-----------------------------------')
    print('1. Add a new task')
    print('2. Delete')
    print('3. List tasks')
    print('4. Quit')

    choice = input (' Enter your choice:')

    if (choice == '1'):
        addTask()
    elif (choice == '2'):
        deleteTask()
    elif (choice == '3'):
        listTasks()
    elif (choice == '4'):
        break

    else:
        print('Invalid input, Please try again.')