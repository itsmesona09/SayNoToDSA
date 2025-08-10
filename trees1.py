# define a class TreeNode representing a node in a tree ds
# each node holds a data and a list of child nodes (children)
class TreeNode:
    # init method => initializes a node
    #  data => value stored in the node
    # pointer => empty list intended to store the references to child nodes
    # classDiagram
    # class TreeNode {
        # data
        # pointer : list
    # }
    def __init__(self, data):
        self.data = data
        self.children = []

treeNode = TreeNode(5)
print(treeNode.data)
print(treeNode.children)