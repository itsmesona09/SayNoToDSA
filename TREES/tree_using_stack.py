class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    def in_order(self, root):
        if not root:
            return []
        
        stack = []
        res = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            
        return res
        
    def pre_order(self, root):
        if not root:
            return []
        
        stack = [root]
        res = []
        
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        return res

    def post_order(self, root):
        if not root:
            return []
        
        stack = [root]
        res = []
        curr = root
        
        while stack:
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            curr = stack.pop()
            res.append(curr.val)
        
        return res
        
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