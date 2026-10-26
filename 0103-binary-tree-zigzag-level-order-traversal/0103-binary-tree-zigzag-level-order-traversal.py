from collections import deque
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        is_left_to_right = True
        
        while queue:
            size = len(queue)
            # Pre-allocate array of fixed size to map items directly via index, 
            # avoiding expensive reversing or list insertions.
            current_level = [0] * size
            
            for i in range(size):
                node = queue.popleft()
                
                # Determine placement index: 
                # Left-to-right fills normally (0, 1, 2...)
                # Right-to-left fills backwards (size - 1 - i)
                index = i if is_left_to_right else size - 1 - i
                current_level[index] = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
            is_left_to_right = not is_left_to_right  # Flip direction flag
            
        return result