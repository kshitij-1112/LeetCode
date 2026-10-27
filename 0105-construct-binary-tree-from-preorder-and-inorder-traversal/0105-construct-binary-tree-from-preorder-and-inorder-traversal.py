# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def buildTree(
      self, preorder: List[int], inorder: List[int]
  ) -> Optional[TreeNode]:
    # Pre-build a hash map for O(1) lookups of inorder indices
    in_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0

    def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
      nonlocal pre_idx

      # Base case: if there are no elements to construct subtrees
      if in_left > in_right:
        return None

      # Get the current root value from preorder and advance the pointer
      root_val = preorder[pre_idx]
      pre_idx += 1
      root = TreeNode(root_val)

      # Find the root's index in inorder using the hash map in O(1) time
      idx = in_map[root_val]

      # Recursively build left and right subtrees
      # Left subtree must be built first because preorder is Root -> Left -> Right
      root.left = helper(in_left, idx - 1)
      root.right = helper(idx + 1, in_right)

      return root

    return helper(0, len(inorder) - 1)