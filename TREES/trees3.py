class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        
class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, data, parent_data = None):
        node = TreeNode(data)
        if not self.root:
            self.root = node
            return
        
        # if tree is empty, it sets the new node as root
        # otherwise searches for the parent node with value parent_data
        parentNode = self.findNode(parent_data, self.root)
        if not parentNode:
            print("Parent node not found")
            return
        parentNode.children.append(node)
                
    def findNode(self, data, node):
        # data => value you are searching for in the tree
        # node => instance which the search starts (root)
        
        # graph TD
        # Root["node"]
        # Child1["child 1"]
        # Child2["child 2"]
        # Root --> Child1
        # Root --> Child2

        # checks if the curr node's data matches the target value
        # if it does, it returns the node
        if node.data == data:
            return node
        
        # checks for all the children of that node
        # recursively checks for all children
        for child in node.children:
            foundNode = self.findNode(data, child)
            # if found return the first matching node
            if foundNode:
                return foundNode
            
        # if nothing matched
        return None

tree = Tree()
tree.add(5)
# add a new node 6 with the value 5 in the tree
# calls add with data = 6 and parent data = 5
tree.add(6, 5)
tree.add(7, 6)
tree.add(9, 5)
