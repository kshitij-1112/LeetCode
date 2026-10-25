class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Using a standard list as a stack for faster push/pop operations
        stack = [(root.left, root.right)]
        
        while stack:
            t1, t2 = stack.pop()
            
            # If both nodes are None, continue
            if not t1 and not t2:
                continue
            # If one is None or values don't match, it's not symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # Push mirror pairs onto the stack
            stack.append((t1.left, t2.right))
            stack.append((t1.right, t2.left))
            
        return True