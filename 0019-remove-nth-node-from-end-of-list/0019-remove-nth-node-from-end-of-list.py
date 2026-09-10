# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Create a gap of n nodes
        for _ in range(n):
            fast = fast.next

        # Move until fast is at the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next
