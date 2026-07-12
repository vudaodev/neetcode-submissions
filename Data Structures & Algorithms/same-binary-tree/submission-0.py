# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # We have to traverse both linked lists, check every value to see if we have the same subtree.
        # pre-order traversal makes the most sense
        # Traverse both trees simultaneously:
            # We would have to use extra memory if we traversed one after the other
            # It's also possible for 2 different trees to produce the same array
            # E.g: 
            # 2.            1
            #1  3              2
            #                     3
        # if the value at a node is ever different for p and q, we return false
        # returning false once in the chain would return false overall