# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def inorder(node):
            # Base case: Null values
            if not node:
                return
            # Recursive case: left child call, print current node's val, right child call
            inorder(node.left)
            res.append(node.val) 
            inorder(node.right)
        
        inorder(root)
        return res