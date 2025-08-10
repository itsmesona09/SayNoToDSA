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
    
    # defines a method add to add new node containing data to tree
    def add(self, data):
        # it creates a new node TreeNode instance with the given data
        # it doesn't specify how and where the new node is added
        # it only creates a new node
        node = TreeNode(data)
        
tree = Tree()
tree.add(5)