class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        # swap children
        root.left, root.right = root.right, root.left
        
        # recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root