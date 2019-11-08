class SearchTree:
    # методы начинающиеся с "_" считать protected
    root = None

    @staticmethod
    def _append(input_data, node):
        if node.data == input_data:
            return
        elif node.data > input_data:
            if node.left is None:
                node.left = Node(input_data, node)
            else:
                SearchTree._append(input_data, node.left)
        else:
            if node.right is None:
                node.right = Node(input_data, node)
            else:
                SearchTree._append(input_data, node.right)

    def append(self, input_data):
        if self.root is None:
            self.root = Node(input_data, None)
        else:
            SearchTree._append(input_data, self.root)

    @staticmethod
    def _find(input_data, node):
        if node.data == input_data:
            return node
        elif node.data > input_data:
            if node.left is None:
                return False
            else:
                return SearchTree._find(input_data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return SearchTree._find(input_data, node.right)

    def find(self, input_data):
        return SearchTree._find(input_data, self.root)

    def delete_element(self, input_data):
        element = self.find(input_data)
        # проверка на наличие элемента
        if not element:
            print("данного элемента нет в дереве")
            return
        # когда эелемент - корень
        if element == self.root:
            a = element.right
            while not (a.left is None):
                a = a.left
            if a == element.right:
                a.left = element.left
            else:
                a.parent.left = a.right
                a.left = element.left
                a.right = element.right
            a.parent = None
            self.root = a
        # когда нет дочерних элементов
        elif element.left is None and element.right is None:
            if element.parent.data > element.data:
                element.parent.left = None
            else:
                element.parent.right = None
        # когда только правый дочерний элемент
        elif element.left is None:
            if element.parent.data > element.data:
                element.parent.left = element.right
            else:
                element.parent.right = element.right
        # когда только левый дочерний элемент
        elif element.right is None:
            if element.parent.data > element.data:
                element.parent.left = element.left
            else:
                element.parent.right = element.left
        # когда оба дочерних элемента
        else:
            a = element.right
            while a.left is not None:
                a = a.left
            a.parent.left = a.right
            a.right = element.right
            a.left = element.left
            if element.parent.data > element.data:
                element.parent.left = a
            else:
                element.parent.right = a

    # обходы дерева
    @staticmethod
    def _infix_traverse(node):
        if node.left is not None:
            SearchTree._infix_traverse(node.left)
        print(node.data)
        if not (node.right is None):
            SearchTree._infix_traverse(node.right)

    def infix_traverse(self):
        if self.root is not None:
            SearchTree._infix_traverse(self.root)
        else:
            print("Дерево пусто")

    @staticmethod
    def _prefix_traverse(node):
        print(node.data)
        if node.left is not None:
            SearchTree._prefix_traverse(node.left)
        if not (node.right is None):
            SearchTree._prefix_traverse(node.right)

    def prefix_traverse(self):
        if self.root is not None:
            SearchTree._prefix_traverse(self.root)
        else:
            print("Дерево пусто")

    @staticmethod
    def _postfix_traverse(node):
        if node.left is not None:
            SearchTree._postfix_traverse(node.left)
        if not (node.right is None):
            SearchTree._postfix_traverse(node.right)
        print(node.data)

    def postfix_traverse(self):
        if self.root is not None:
            SearchTree._postfix_traverse(self.root)
        else:
            print("Дерево пусто")


# Узел дерева
class Node:
    parent = None
    left = None
    right = None
    data = None

    def __init__(self, data, parent):
        self.parent = parent
        self.data = data
