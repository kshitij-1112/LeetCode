# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def dfs(node, target, path):
            path.append(node.val)
            
            # If it's a leaf node, check condition
            if not node.left and not node.right:
                if target == node.val:
                    res.append(path[:]) # O(K) slice copy
            else:
                # Guard checks avoid pushing None frames onto the call stack
                if node.left:
                    dfs(node.left, target - node.val, path)
                if node.right:
                    dfs(node.right, target - node.val, path)
            
            # Backtrack
            path.pop()
            
        dfs(root, targetSum, [])
        return res