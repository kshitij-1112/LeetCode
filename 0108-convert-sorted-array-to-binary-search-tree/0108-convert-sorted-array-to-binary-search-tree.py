# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Create a root placeholder
        root = TreeNode(0)
        # Stack stores tuples of: (current_node, left_index, right_index)
        stack = [(root, 0, len(nums) - 1)]
        
        while stack:
            node, left, right = stack.pop()
            
            # Find the middle index using bitwise shift for optimal speed
            mid = (left + right) >> 1
            node.val = nums[mid]
            
            # Handle left subtree
            if left <= mid - 1:
                node.left = TreeNode(0)
                stack.append((node.left, left, mid - 1))
                
            # Handle right subtree
            if mid + 1 <= right:
                node.right = TreeNode(0)
                stack.append((node.right, mid + 1, right))
                
        return root