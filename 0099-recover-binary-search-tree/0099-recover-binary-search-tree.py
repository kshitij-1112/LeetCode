
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        curr = root

        while curr:
            if curr.left is None:
                # Visit current node
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr

                prev = curr
                curr = curr.right

            else:
                # Find inorder predecessor
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if pred.right is None:
                    # Create temporary thread
                    pred.right = curr
                    curr = curr.left
                else:
                    # Remove temporary thread and visit current
                    pred.right = None

                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        # Swap the two misplaced values
        first.val, second.val = second.val, first.val
