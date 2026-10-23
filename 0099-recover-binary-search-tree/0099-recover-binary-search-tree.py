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
        # state container: [first, second, prev]
        state = [None, None, None]
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            prev = state[2]
            if prev and prev.val > node.val:
                if not state[0]:
                    state[0] = prev
                    state[1] = node
                else:
                    state[1] = node
            state[2] = node
            
            inorder(node.right)
            
        inorder(root)
        
        if state[0] and state[1]:
            state[0].val, state[1].val = state[1].val, state[0].val