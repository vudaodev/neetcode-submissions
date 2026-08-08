# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
# SAME TREE HELPER - DFS
    # return True if:
        # root1 and root2 both don't exist
    # return false if:
        # root1 exists but root2 doesn't
        # root2 exists but root1 doesn't
    # return result of going left AND right

Go through all nodes within 'root'
    For each node, check whether we can start there to get a subtree identical to subroot.
    We'll use a helper function that checks whether two trees are the same.

'''
class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1: 
        if not root:
            return False
        # Base case 2:
        if root.val == subRoot.val and self.isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        