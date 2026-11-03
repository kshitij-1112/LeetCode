# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # Choose: add current node to path
            path.append(node.val)
            current_sum += node.val
            
            # If it's a leaf node and matches the target sum, save a copy of the path
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path)) # O(K) copy where K is path length
            else:
                # Explore children
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
            
            # Unchoose (Backtrack): remove current node before returning to parent
            path.pop()
            
        dfs(root, 0, [])
        return result