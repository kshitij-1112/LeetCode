# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Put the first node of every non-empty list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)

            # Add smallest node to result
            tail.next = node
            tail = node

            # Add next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next