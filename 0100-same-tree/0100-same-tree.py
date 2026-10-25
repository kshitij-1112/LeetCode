from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # If both are None, continue to next pair
            if not node1 and not node2:
                continue
            # If one is None or values don't match, they aren't the same
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Append left and right children pairs
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
            
        return True