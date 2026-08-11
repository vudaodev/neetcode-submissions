# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
level order traversal
empty array called res 
Use a queue to process all of the nodes in the correct order
For each level, we pick the rightmost node, and add it's value to res
Return res 
'''
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            level_len = len(queue)
            for i in range(level_len):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if i == level_len - 1:
                    res.append(curr.val)
        
        return res