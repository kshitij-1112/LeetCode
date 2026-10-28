class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        in_map = {val: i for i, val in enumerate(inorder)}
        post_idx = len(postorder) - 1
        
        def helper(in_left: int, in_right: int) -> TreeNode | None:
            nonlocal post_idx
            if in_left > in_right:
                return None
            
            # Get the current root from postorder and decrement the pointer
            root_val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(root_val)
            
            # Find root position in inorder to split left and right subtrees
            index = in_map[root_val]
            
            # Build right subtree first (due to reverse postorder processing)
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root

        return helper(0, len(inorder) - 1)