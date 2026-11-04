# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        
        while current:
            if current.left:
                # 1. Find the rightmost node of the left subtree (predecessor)
                prev = current.left
                while prev.right:
                    prev = prev.right
                
                # 2. Connect the original right subtree to the predecessor's right
                prev.right = current.right
                
                # 3. Shift the left subtree to the right child and clear the left child
                current.right = current.left
                current.left = None
                
            # 4. Move to the next node on the right
            current = current.right