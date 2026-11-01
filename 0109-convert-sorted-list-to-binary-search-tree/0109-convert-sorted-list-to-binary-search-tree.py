# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Phase 1: Convert the linked list into a Python array for O(1) index access
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
            
        # Phase 2: Recursively build the BST using index boundaries
        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) >> 1
            
            # Instantiate the root and construct subtrees concurrently using slicing indices
            root = TreeNode(
                nums[mid], 
                build_tree(left, mid - 1), 
                build_tree(mid + 1, right)
            )
            return root
            
        return build_tree(0, len(nums) - 1)