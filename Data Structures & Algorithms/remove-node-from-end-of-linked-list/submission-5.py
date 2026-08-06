# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Recursion: 
Recursively go to the end. 
Decrement n as you unwind back up. 
when n == 0: remove required node
-
[4,3,2,1], n = 4
We start with a dummy node that goes before the head.
We return dummy.next. 
'''
class Solution:
    def remove(self, node, n):
        # Base case: We've reached the end and we're winding back up
        if not node:
            return None            
        # Recursive case:
        node.next = self.remove(node.next, n)
        n[0] -= 1
        if n[0] == 0:
            return node.next # skips the node to be removed 
        return node
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.remove(head,[n])
        
        



        