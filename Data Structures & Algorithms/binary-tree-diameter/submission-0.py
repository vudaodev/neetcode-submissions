# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def findD(node):
            if not node:
                return 0
            left, right = findD(node.left), findD(node.right)

            nonlocal maxD
            maxD = max(maxD, left + right) #Update max Diameter
            return 1 + max(left, right) #Return height

        findD(root) 

        return maxD
        
                 
        
