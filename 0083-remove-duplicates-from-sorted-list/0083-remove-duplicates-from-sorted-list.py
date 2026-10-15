# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the duplicate node by pointing to the next-next node
                curr.next = curr.next.next
            else:
                # Move forward only if there is no duplicate
                curr = curr.next
                
        return head