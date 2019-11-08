from SearchTree import SearchTree
tree = SearchTree()
while True:
    print("""Введите команду из предложенных:
    Добавить(1) {значение}
    Удалить(2) {значение}
    Найти(3) {значение}
    Обход прямой(1)
    Обход обратный(2)
    Обход концевой(3)
    Стоп(4)""")
    command = input().split(" ")
    command[0] = command[0].lower()
    if command[0] == "добавить" or command[0] == "1":
        tree.append(int(command[1]))
    elif command[0] == "удалить" or command[0] == "2":
        tree.delete_element(int(command[1]))
    elif command[0] == "найти" or command[0] == "3":
        print(tree.find(int(command[1])))
    elif command[0] == "обход" :
        if command[1].lower() == "прямой" or command[1] == "1":
            tree.infix_traverse()
        elif command[1].lower() == "обратный" or command[1] == "2":
            tree.prefix_traverse()
        elif command[1].lower() == "концевой" or command[1] == "3":
            tree.postfix_traverse()
    elif command[0] == "стоп" or command[0] == "4":
        break
    else:
        print("Я не знаю такой комманды")