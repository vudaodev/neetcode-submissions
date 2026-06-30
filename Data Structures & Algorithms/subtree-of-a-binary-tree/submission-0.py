# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q: 
                return False
            if p.val != q.val: 
                return False
            # recursive case: returns true if trees as the same 
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        # Base cases:
        # 1: 
        if not root:
            return False
        # 2: Perform same tree
        if root.val == subRoot.val and isSameTree(root,subRoot):
            return True 
            
        # Recursive case: if True is returned, the subroot exists
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)