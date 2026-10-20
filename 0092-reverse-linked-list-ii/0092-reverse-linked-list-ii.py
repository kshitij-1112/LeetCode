# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # A dummy node handles edge cases where left = 1 (head changes)
        dummy = ListNode(0, head)
        prev = dummy

        # 1. Move 'prev' to the node right before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        # 2. 'curr' points to the first node of the sublist to be reversed
        curr = prev.next

        # 3. Iteratively reverse the sublist using standard pointer manipulation
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next