"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        # 'curr' traverses the current level like a linked list
        curr = root
        
        # We loop until we've processed all levels
        while curr:
            # Dummy node to act as the starting point of the next level
            dummy = Node(0)
            # 'tail' builds the linked list for the next level as we go
            tail = dummy
            
            # Iterate through the nodes of the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                # Move to the next node on the current level
                curr = curr.next
            
            # Move down to the head of the newly constructed next level
            curr = dummy.next
            
        return root