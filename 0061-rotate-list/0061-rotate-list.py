# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        # Edge cases: empty list, single element list, or zero rotation
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length and locate the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Optimize k if it's greater than the list length
        k %= length
        if k == 0:
            return head
        
        # Step 3: Connect tail to head to form a circular linked list
        tail.next = head
        
        # Step 4: Find the new tail, which is at (length - k - 1) steps from head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Step 5: Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head