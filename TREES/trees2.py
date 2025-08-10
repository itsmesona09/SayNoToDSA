class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
    
    # defines a method add to add new node containing data to tree
    def add(self, data):
        # it creates a new node TreeNode instance with the given data
        # it doesn't specify how and where the new node is added
        # it only creates a new node
        node = TreeNode(data)
        
        # if self.root is None, it means the tree is empty
        # assigns the new node as the root
        # short cut for if self.root is None:
        if not self.root:
            self.root = node
            # why return is used?
            # it doesn't execute the codes below that
            return
        
        # if self.root is not None, it means the tree is not empty
        # it adds the new node as a child of the root
        self.root.children.append(node)
tree = Tree()
tree.add(5)
tree.add(6)

# graph TD
#     Root["5"]
#     Child1["6"]
#     Root --> Child1

# prints the data stored in the root node of a tree
print(tree.root.data)
# prints the first child node
# this only adds children directly to the root node
# there is no logic for adding children to other nodes or deeper tree structures
print(tree.root.children[0].data)