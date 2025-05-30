todos = []

while True:
    user_action = input("Type add, show or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display' | 'Show':
            for item in todos:
                print(item.title())
            
            '''print(todos)
            i = 0
            while i<todos.__len__():
                print(i, ') ',todos[i].title(), sep="", end=", ")
                i += 1
            print()'''

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
