from collections import deque

class MaxDepth:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def max_depth(self, root):
        depth = 0
        if not root:
            return depth
        
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth
    
maxdepth = MaxDepth()
root = MaxDepth(3, MaxDepth(9), MaxDepth(20, MaxDepth(15), MaxDepth(7)))
print(maxdepth.max_depth(root))