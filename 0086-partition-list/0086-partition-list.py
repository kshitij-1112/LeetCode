# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create dummy heads for the two partitions (< x and >= x)
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to track the tails of the two lists
        before = before_head
        after = after_head
        
        # Traverse the original list once
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
            
        # Terminate the 'after' list to prevent infinite cycles
        after.next = None
        
        # Connect the end of the 'before' list to the start of the 'after' list
        before.next = after_head.next
        
        return before_head.next