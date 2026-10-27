
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        stack = [(root, 1)]
        depth = 0

        while stack:
            node, level = stack.pop()
            depth = max(depth, level)

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return depth
