# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    curr = root

    while curr or stack:
      # Reach the leftmost node of the current node
      while curr:
        stack.append(curr)
        curr = curr.left

      # Current must be null at this point, so pop from stack
      curr = stack.pop()
      result.append(curr.val)

      # We have visited the node and its left subtree. Now, visit right subtree.
      curr = curr.right

    return result