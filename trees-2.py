class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# define a class Tree that initializes an empty root
class Tree:
    # init method takes no parameters except self
    # self.root = None will be set when an instance of this class is created
    # classDiagram
    # class SomeClass {
    #     root
    # }
    def __init__(self):
        self.root = None