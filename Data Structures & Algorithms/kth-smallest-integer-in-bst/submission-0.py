# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
In order traversal
'values' array tracks node vals (asc order)
Return the k-th value in values
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def helper(node):
            if not node:
                return 
            
            helper(node.left)
            values.append(node.val)
            helper(node.right)

        helper(root)

        return values[k-1]