# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Inorder traversal
Decrement a count variable
    - starts at k
    - when count == 0, return value
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        res = [None]

        def helper(node):
            if not node or res[0] is not None:
                return 

            helper(node.left)

            if res[0] is not None:
                return 

            count[0] -= 1
            if count[0] == 0:
                res[0] = node.val
                return 

            helper(node.right)

        helper(root)
        return res[0]
