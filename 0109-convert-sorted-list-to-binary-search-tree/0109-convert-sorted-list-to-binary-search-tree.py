
class Solution:
    def sortedListToBST(self, head):
        # Find the length of the linked list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Pointer to traverse the linked list
        self.curr = head

        def build(size):
            if size <= 0:
                return None

            # Build left subtree
            left = build(size // 2)

            # Current list node becomes the root
            root = TreeNode(self.curr.val)
            root.left = left

            # Move linked list pointer forward
            self.curr = self.curr.next

            # Build right subtree
            root.right = build(size - size // 2 - 1)

            return root

        return build(n)
