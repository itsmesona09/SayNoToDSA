class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right =right
    
class Tree:
    def in_order(self, root):
        if not root:
            return []
        
        return (
            self.in_order(root.left) +
            [root.val] +
            self.in_order(root.right)
        )
        
    def pre_order(self, root):
        if not root:
            return []

        return (
            [root.val] + 
            self.pre_order(root.left) +
            self.pre_order(root.right)
        )
        
    def post_order(self, root):
        if not root:
            return []
        
        return (
            self.post_order(root.left) + 
            self.post_order(root.right) +
            [root.val]
        )

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

tree = Tree()
print("IN-ORDER: ", tree.in_order(root))
print("PRE-ORDER: ",tree.pre_order(root))
print("POST-ORDER: ",tree.post_order(root))