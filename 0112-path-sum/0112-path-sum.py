# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty, no path exists
        if not root:
            return False
        
        # If it's a leaf node, check if the remaining target matches its value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recurse down left and right subtrees with the updated remaining sum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)