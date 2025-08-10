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
        
        parentNode = self.findNode(parent_data, self.root)
        if not parentNode:
            print("Parent node not found")
            return
        parentNode.children.append(node)
                
    def findNode(self, data, node):
        if node.data == data:
            return node
        
        for child in node.children:
            foundNode = self.findNode(data, child)
            if foundNode:
                return foundNode
            
        return None
    
    # recursively prints the tree corresponding to the depth
    def display(self, depth = 1, node = None):
        # if node is not given, it uses the root
        if not node:
            node = self.root
        
        # prints the nod's data by the given depth
        print(" " * depth, node.data)
        # recursively calls the display function for each child inc depth
        for child in node.children:
            self.display(depth + 3, child)

tree = Tree()
tree.add(1)
tree.add(2, 1)
tree.add(3, 1)
tree.add(4, 1)
tree.add(5, 2)
tree.add(6, 2)
tree.add(7, 3)
tree.add(8, 3)

tree.display(node = tree.root)