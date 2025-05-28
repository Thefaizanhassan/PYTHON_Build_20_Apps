user_prompt = "Enter the todo: "

todos = []
while(input("Add a new todo(Y/N): ") == ('Y' or 'y') ):
    todo = input(user_prompt)
    todos.append(todo)
i = 0
while i<todos.__len__():
    print(todos[i].title())
    i += 1

# print(len(todo1))