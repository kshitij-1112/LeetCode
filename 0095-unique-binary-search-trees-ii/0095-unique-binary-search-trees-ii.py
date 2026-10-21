# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right


class Solution:

  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    memo = {}

    def helper(start, end):
      if start > end:
        return [None]
      if (start, end) in memo:
        return memo[(start, end)]

      all_trees = []
      for i in range(start, end + 1):
        # Generate all left and right subtrees recursively
        left_trees = helper(start, i - 1)
        right_trees = helper(i + 1, end)

        # Combine each combination of left and right subtrees with root `i`
        for l in left_trees:
          for r in right_trees:
            current_node = TreeNode(i, l, r)
            all_trees.append(current_node)

      memo[(start, end)] = all_trees
      return all_trees

    return helper(1, n) if n else []