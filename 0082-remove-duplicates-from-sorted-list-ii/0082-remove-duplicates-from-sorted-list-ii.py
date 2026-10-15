# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (e.g., when the head itself is a duplicate)
        dummy = ListNode(0, head)
        prev = dummy
        
        curr = head
        while curr:
            # If current node has a duplicate ahead
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                # Skip all nodes with this duplicate value
                while curr and curr.val == dup_val:
                    curr = curr.next
                # Link prev to the first non-duplicate node
                prev.next = curr
            else:
                # No duplicate, advance prev pointer
                prev = curr
                curr = curr.next
                
        return dummy.next