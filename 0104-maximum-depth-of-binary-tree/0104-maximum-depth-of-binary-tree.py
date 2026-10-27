class Solution:

  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    # Local helper avoids 'self.' lookup overhead
    def dfs(node):
      # Pre-check children to prevent calling dfs() on None nodes
      left = dfs(node.left) if node.left else 0
      right = dfs(node.right) if node.right else 0
      return 1 + (left if left > right else right)

    return dfs(root)