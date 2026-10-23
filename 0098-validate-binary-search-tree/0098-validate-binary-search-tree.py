class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev_val = None
        curr = root
        
        while curr:
            if not curr.left:
                # Process current node
                if prev_val is not None and curr.val <= prev_val:
                    return False
                prev_val = curr.val
                curr = curr.right
            else:
                # Find the inorder predecessor of curr
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    # Make curr the right child of its predecessor
                    pred.right = curr
                    curr = curr.left
                else:
                    # Revert the changes made to restore the original tree structure
                    pred.right = None
                    if prev_val is not None and curr.val <= prev_val:
                        return False
                    prev_val = curr.val
                    curr = curr.right
                    
        return True