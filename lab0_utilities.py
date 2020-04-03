class Word:
    def __init__(self, key, definition):
        self.name = key
        self.definition = definition

    def __str__(self):
        return self.name


class Node:
    def __init__(self, word, left=None, right=None, parent=None, height=1, bf=0):
        self.val = [word]
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height
        self.bf = bf
        self._val = str(word)


class Node2:
    def __init__(self, bst, left=None, right=None, parent=None, height=1, bf=0):
        self.val = bst
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height
        self.bf = bf
        self._val = bst.root._val[0]
