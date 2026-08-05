# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Singly linked list
We need to know how many nodes are in the list so that we can remove the nth from last node
We need to keep track of node before and node after the one we're removing so that we can join them.

1. Count number of nodes
2. Find node before, and node after (N-n-1)
3. Link node before with node after (N-n+1)

If there are N nodes, we are removing the (N-n)th node -> 0 indexing
# CONSIDER EDGE CASE OF REMOVING LAST VALUE

'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Count number of Nodes
        N, curr = 0, head
        while curr:
            N += 1
            curr = curr.next
        # 2.  Find the node before and the node after
        target = N - n
        # a. Edgecase: We're removing the 1st node
        if target == 0:
            head = head.next
            return head
        # b. Normalcase:
        curr, index = head, 0
        while index < target - 1:
            curr = curr.next 
            index += 1
        # 3. Remove N-nth index 
        curr.next = curr.next.next
        return head

