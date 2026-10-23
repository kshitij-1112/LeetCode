# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # Base case: an empty node is a valid BST
            if not node:
                return True
            
            v = node.val
            
            # Check current node against the allowed boundaries
            if low is not None and v <= low:
                return False
            if high is not None and v >= high:
                return False
            
            # Recursively validate left and right subtrees with updated bounds
            return validate(node.left, low, v) and validate(node.right, v, high)
        
        return validate(root, None, None)