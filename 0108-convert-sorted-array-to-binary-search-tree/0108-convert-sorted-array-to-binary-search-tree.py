# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Find the middle index (equivalent to (left + right) // 2)
            mid = (left + right) >> 1
            
            # Create the root node with the middle element
            root = TreeNode(nums[mid])
            
            # Recursively construct left and right subtrees
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)
            
            return root
            
        return build_tree(0, len(nums) - 1)