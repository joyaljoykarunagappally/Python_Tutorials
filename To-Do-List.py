todo_list = []


def addList():
    item = input("Enter a new task : ")
    todo_list.append(item)
    print(f'{item} added successfully')


def displayList():
    print("--------------------")
    print("TO DO LIST")
    print("--------------------")
    for index, item in enumerate(todo_list, start=1):
        print(f'{index} - {item}')


def removeList():
    displayList()
    index = int(input('Enter your item number to remove : ')) - 1
    if 0 <= index <= len(todo_list):
        removeditem = todo_list.pop(index)
        print(f"{removeditem} removed from the list")
    else:
        print("Invalid Input")


while True:
    print("****************")
    print("To-Do List")
    print("****************")
    print("1.ADD NEW TASK")
    print("2.DISPLAY TASKS")
    print("3.REMOVE TASK")
    print("4.EXIT")

    option = input("Select your option : ")

    if option == '1':
        addList()
    elif option == '2':
        displayList()
    elif option == '3':
        removeList()
    elif option == '4':
        print("Thank you (: ")
        break
    else:
        print("Invalid Entry")
