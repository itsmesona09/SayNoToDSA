class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    def bfs(self, root):
        # check if the root node is empty, if empty return []
        if not root:
            return []
        
        # uses a queue to process nodes level by level
        # creates a list containing a root node
        queue = [root]
        res = []
        
        # until the queue is empty
        while queue:
            # removes the element at index 0
            curr = queue.pop(0)
            # append the value of the current node
            res.append(curr.val)
            
            # until the left node, append the queue with the left node
            if curr.left:
                queue.append(curr.left)
            # until the right node, append the queue with the right node
            if curr.right:
                queue.append(curr.right)
                
        return res
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

tree = Tree()
print("BFS TRAVERSAL: ",tree.bfs(root))