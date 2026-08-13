# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Post order dfs -> left, right, process current node
Use recursion where we return up the binary tree:
    whether node is valid
    largest value in subtree
    smallest value in subtree

(valid, smallest, largest)
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node):   
            if not node: 
                return (True,float('inf'), float('-inf'))
            # tuple (valid, smallest, largest)
            left = validate(node.left) 
            right = validate(node.right)

            # Valid if:
                # both subtrees are valid
                # greatest in left < node.val < smallest in right
            valid = left[0] and right[0] and node.val > left[2] and node.val < right[1]

            return(valid, min(left[1],right[1],node.val), max(left[2],right[2],node.val))

        return validate(root)[0]