class InvBinaryTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
        
    def invertbinTree(self, root):
        if not root:
            return None
        
        root.left, root.right = self.invertbinTree(root.right), self.invertbinTree(root.left)
        
        return root
    
inv = InvBinaryTree()
root = InvBinaryTree(4, InvBinaryTree(2, InvBinaryTree(1), InvBinaryTree(3)), InvBinaryTree(7, InvBinaryTree(6), InvBinaryTree(9)))
root = inv.invertbinTree(root)

print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)