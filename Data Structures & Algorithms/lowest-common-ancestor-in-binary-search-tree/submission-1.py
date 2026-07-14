'''
We know that we have the LCF if 2 of these conditions are true: 
    One variable is to the left of node 
    One variable is to the right of node 
or if: 
    We encounter p or q

For a node: if one of p/q is less, and the other is more, we have LCF
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findlcf(node):
            # if not node: return 

            P,Q = p.val, q.val
            condition1 = (node.val > P and node.val < Q)
            condition2 = (node.val < P and node.val > Q)
            condition3 = (node.val == P or node.val == Q)
            if condition1 or condition2 or condition3:
                return node
            
            if node.val > P and node.val > Q: # Go left
                return findlcf(node.left)
            if node.val < P and node.val < Q: # Go right
                return findlcf(node.right)
        return findlcf(root)
        

