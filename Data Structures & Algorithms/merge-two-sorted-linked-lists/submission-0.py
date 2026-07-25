# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Input: 2 lists
Output: Head of the new sorted list

We are sorting in ascending order
Conflict/ equal values? -> Choose list 1 over list 2.
We need to keep track of:
- next value in list1/ list2
- Head of our 'merged' LL
- current value in our 'merged' LL (so that we can add more values to it from l1/2)

Edge cases:
- 2 empty lists, return empty lists (early return @ top)
- if 1 list is finishes before the other, append rest of other list
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        dummy = ListNode() # We return dummy.next at the end.
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                # tmp = list1.next # save tmp so we can reassign start of l1
                current.next = list1 #point current to list 1
                # Move pointers
                current = current.next
                list1 = list1.next
            else:
                # tmp = list2.next
                current.next = list2
                current = current.next
                list2 = list2.next

        if not list1:
            current.next = list2
        if not list2: 
            current.next = list1

        return dummy.next
