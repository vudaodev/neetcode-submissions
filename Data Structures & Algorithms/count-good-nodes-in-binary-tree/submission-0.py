# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Node x is a good node if: no nodes greater than x from the root.
Keep track of good nodes 
We will always have at least one good node, the root.
DFS strategy (pre-order)
For each node:
 - If node value >= current_max_of_path, it is a good node => increment count
 - Update the current_max_of_path
 - traverse children
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def findGoodNodes(node, current_max = -101):
            if not node:
                return None

            if node.val >= current_max:
                nonlocal res
                res += 1
            
            current_max = max(current_max, node.val)

            findGoodNodes(node.left, current_max)
            findGoodNodes(node.right, current_max)
        
        findGoodNodes(root)
        return res