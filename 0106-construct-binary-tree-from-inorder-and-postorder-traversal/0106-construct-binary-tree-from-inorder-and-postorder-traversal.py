# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        # Map values to their indices in inorder for O(1) lookups
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left: int, in_right: int, post_left: int, post_right: int) -> TreeNode | None:
            # Base case: if there are no elements to construct the subtree
            if in_left > in_right or post_left > post_right:
                return None
            
            # The last element in postorder is the current root
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            # Find the root's index in inorder
            index = in_map[root_val]
            
            # Number of elements in the left subtree
            left_size = index - in_left
            
            # Recursively build left and right subtrees
            root.left = helper(in_left, index - 1, post_left, post_left + left_size - 1)
            root.right = helper(index + 1, in_right, post_left + left_size, post_right - 1)
            
            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)