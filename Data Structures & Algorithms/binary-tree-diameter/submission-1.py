# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
- keep a global record of max_diameter
- for each node x, keep a note of max_left and max_right
    - diameter of x = max_left + max_right 
    - compare diameter to global, update if needed
- return max_diameter 
- if you have a leaf node, return 0, else add 1 

'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # curr_diam = left height and right height
        max_diameter = 0
        def find_max(node):
            # leaf node, return 0
            if not node:
                return 0

            # update max
            nonlocal max_diameter 
            max_diameter = max(max_diameter, find_max(node.left) + find_max(node.right))

            # find current depth
            depth = max(find_max(node.left), find_max(node.right)) + 1
            # return current depth
            return depth

        find_max(root)
        return max_diameter

        