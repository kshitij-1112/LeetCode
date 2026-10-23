# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        curr = root
        first = second = prev = None
        
        while stack or curr:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the node
            curr = stack.pop()
            
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                    second = curr
                else:
                    second = curr
                    
            prev = curr
            curr = curr.right
            
        # Swap the values to recover the BST
        if first and second:
            first.val, second.val = second.val, first.val