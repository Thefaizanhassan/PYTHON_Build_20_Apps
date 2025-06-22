while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('./files/todo.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)

            file = open('./files/todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display' | 'Show':
            file = open('./files/todo.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(index + 1, '-', item.title(), sep="",end="")
            # print(f"Length is {len(todos)}")
            '''print(todos)
            i = 0
            while i<todos.__len__():
                print(i, ') ',todos[i].title(), sep="", end=", ")
                i += 1
            print()'''
        case 'edit':
            no = int(input("Enter the serial no. of todo to edit: "))
            no -= 1
            todos[no] = input("Enter new todo: ")
        case 'complete':
            number = int(input("Enter the serial no. of todo to mark complete: "))
            todos.pop(number-1)
        case 'exit':
            break
        # case whatever:
        case _:
            print("Enter a valid command.")


# user_prompt = "Enter the todo: "

# todos = []
# while(input("Add a new todo(Y/N): ") == ('Y' or 'y') ):
#     todo = input(user_prompt)
#     todos.append(todo)
# i = 0
# while i<todos.__len__():
#     print(todos[i].title())
#     i += 1

# print(len(todo1))
