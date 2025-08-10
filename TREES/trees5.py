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
    
    def display(self, depth = 1, node = None):
        if not node:
            node = self.root
        
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 3, child)
            
    # removes a node with the specified value from the tree 
    def remove(self, data):
        # checks if the tree is empty
        if not self.root:
            print("Tree is empty")
            return
        
        # if the root is the data to be removed
        if self.root.data == data:
            # set the root node to None and return
            self.root = None
            return
        
        # finds the parent node of the data that is to be removed
        parentNode = self.findParentNode(data, self.root)
        
        # if the parent node is found, iterates through the children
        # and if it matches the child node with the data
        # it removes that child node
        if parentNode:
            for child in parentNode.children:
                if child.data == data:
                    parentNode.children.remove(child)
                    return
                
        # if the above conditions are not met
        # return parent not found
        print("Parent not found")
    
    # recursively searches for the parent node of the node to be deleted
    # data => node to be removed
    # node => parent node of the data
    def findParentNode(self, data, node): 
        # iterates through the children of the node   
        for child in node.children:
            # if the data of the child matches the given data return Node (ie) returns the parent node
            if child.data == data:
                return node
            
            # otherwise find the parent node in each subtrees
            node_found = self.findParentNode(data, child)
            # if the parent node is found return it
            if node_found:
                return node_found
            
        return None
        
tree = Tree()
tree.add(1)
tree.add(2, 1)
tree.add(3, 1)
tree.add(4, 1)
tree.add(5, 2)
tree.add(6, 2)
tree.add(7, 3)
tree.add(8, 3)
tree.remove(8)
tree.display(node = tree.root)