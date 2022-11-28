
class Tree:

    parent = None  # type: Tree
    a = 0  # type: int
    b = 1
    c = 1

    def __init__(self, parent, a, b, c,full_tree) -> None:
        self.parent = parent
        self.a = a
        self.b = b
        self.c = c

        full_tree.append(self)

    def get_sons(self,full_tree) -> list:
        sons = []  # type: list(type = Tree)
        for tree in full_tree:
            if isinstance(tree, Tree):
                if self.equals(tree.parent):
                    sons.append(tree)

        return sons

    @staticmethod
    def get_sons_from_depth(depth: int,full_tree) -> list:
        sons = []  # type: list(type = Tree)

        for tree in full_tree:
            if isinstance(tree, Tree):
                if tree.get_your_depth() == depth:
                    sons.append(tree)

        return sons

    def get_your_depth(self):
        current = 0
        parent = self.parent

        while parent is not None:
            parent = parent.parent

            current = current + 1

        return current

    def equals(self, tree) -> bool:
        if isinstance(tree, Tree):
            if tree.parent == self.parent and tree.a == self.a and tree.b == self.b and tree.c == self.c:
                return True
        return False

    def has_sons(self, full_tree) -> bool:
        for tree in full_tree:
            if isinstance(tree, Tree):
                if tree.parent is not None and tree.parent.equals(self):
                    return True

        return False

    # функция вывода дерева
    def __str__(self):
        # чтобы выводить полный путь до этого сына
        # Например:
        # data: 2 parent: {data: 3 parent: {data: 4 parent: {data: 5 parent: {None}}}}
        parent = "{" + str(self.parent) + "}"

        # Чтобы выводить конкретно отца этого элемента
        # Например:
        # data: 2 parent: 3
        #
        # parent = str(None)
        # if self.parent is not None: parent = str(self.parent.data)

        return "data: [" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + "] parent: " + parent