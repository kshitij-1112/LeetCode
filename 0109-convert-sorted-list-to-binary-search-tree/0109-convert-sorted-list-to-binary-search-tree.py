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
        # Step 1: Count the total number of nodes in the linked list
        def get_length(node: Optional[ListNode]) -> int:
            length = 0
            curr = node
            while curr:
                length += 1
                curr = curr.next
            return length
        
        total_size = get_length(head)
        self.head = head
        
        # Step 2: Recursively build the BST bottom-up using in-order traversal
        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) >> 1
            
            # Recursively build the left subtree
            left_child = build_tree(left, mid - 1)
            
            # Construct the root node using the current linked list head
            root = TreeNode(self.head.val)
            root.left = left_child
            
            # Advance the linked list pointer
            self.head = self.head.next
            
            # Recursively build the right subtree
            root.right = build_tree(mid + 1, right)
            
            return root
            
        return build_tree(0, total_size - 1)