class Solution:

  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    # Local helper eliminates 'self.' lookup overhead
    def dfs(node):
      # Pre-check children: avoids calling dfs() on None nodes entirely
      l = dfs(node.left) if node.left else 0
      r = dfs(node.right) if node.right else 0
      # max() is a C-implemented built-in, making it faster than manual ternaries
      return 1 + (l if l > r else r)

    return dfs(root)