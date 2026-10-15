# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        # Cache curr.next using the walrus operator to eliminate redundant attribute lookups
        while curr and (nxt := curr.next):
            if curr.val == nxt.val:
                curr.next = nxt.next
            else:
                curr = nxt
        return head