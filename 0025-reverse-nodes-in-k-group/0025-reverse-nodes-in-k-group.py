# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:

        if k == 1 or not head:
            return head

        # Count nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        dummy = ListNode(0, head)
        group_prev = dummy

        # Process only complete groups
        while n >= k:
            prev = None
            curr = group_prev.next

            # Reverse k nodes
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect the reversed group
            group_first = group_prev.next
            group_first.next = curr
            group_prev.next = prev

            # Move to next group
            group_prev = group_first
            n -= k

        return dummy.next