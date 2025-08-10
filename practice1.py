# CLASS 1
class TreeNode:
    # create a init method
    # initialize the attributes with default values
    # setting a attribute with a default value and not setting others =, will throw an error
    
    # ERROR:
    # Non-default argument follows default argument
    
    # set val to 0, left and right to None
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right =right
    
# CLASS 2    
class Tree:
    # creating a method with a parameter root
    def in_order(self, root):
        # check if root is empty
        # if empty return []
        if not root:
            return []
        
        # recursively print the left subtrees + root + right subtrees
        return (
            self.in_order(root.left) +
            [root.val] +
            self.in_order(root.right)
        )

# create an instance for TreeNode Class which has init method and creates a tree (left and right and val)
# give a value of 1 as root node
root = TreeNode(1)

# give values to left and right node
root.left = TreeNode(2)
root.right = TreeNode(3)

# give values to the left and right nodes of left subtree
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# give values to the left and right nodes of right subtree
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# create a instance of the Tree class
tree = Tree()
# call the function with the instance of TreeNode class
print(tree.in_order(root))