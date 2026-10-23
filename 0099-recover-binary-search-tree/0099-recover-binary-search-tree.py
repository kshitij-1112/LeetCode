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
        first = second = prev = None
        curr = root
        
        while curr:
            if not curr.left:
                # Check for violation
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                        second = curr
                    else:
                        second = curr
                prev = curr
                curr = curr.right
            else:
                # Find the inorder predecessor of curr
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    # Thread predecessor to curr
                    pred.right = curr
                    curr = curr.left
                else:
                    # Cut the thread and process curr
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                            second = curr
                        else:
                            second = curr
                    prev = curr
                    curr = curr.right
                    
        # Swap the values of the two misplaced nodes to recover the BST
        if first and second:
            first.val, second.val = second.val, first.val