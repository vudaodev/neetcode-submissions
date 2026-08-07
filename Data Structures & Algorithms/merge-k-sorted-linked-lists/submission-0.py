# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1. Add ALL ListNodes to list called 'merged'. Add in the format (node.val, node)
2. Sort 'merged' in asc order
3. Loop 
'''
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                merged.append((curr.val, curr))
                curr = curr.next

        merged.sort(key = lambda _: _[0])
        dummy = ListNode()
        curr = dummy
        for _ in merged:
            curr.next = _[1]
            curr = curr.next
        return dummy.next