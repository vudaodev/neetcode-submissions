# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Step 1: Find the midpoint and split the two lists
Step 2: Reverse the second list
Step 3: Join the two lists together 
[0,1,2,3,4,5,6]
 L R
   L   R
     L     R
       L     R
[0,1,2,3] [4,5,6]
'''  
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split lists:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next # slow is the end of the first list
        slow.next = None # disconnect the two lists
        # Reverse second list:
        prev = None
        while second:
            nxt = second.next # temp pointer to next
            second.next = prev # point second backwards
            # move pointers
            prev = second
            second = nxt
        
        second = prev # loop ends when second == none, so prev is new start of list
        first = head
        # Join lists:
        dummy = ListNode(0)
        curr = dummy
        while first and second:
            fn = first.next
            sn = second.next
            
            curr.next = first
            curr = curr.next
            curr.next = second
            curr = curr.next

            first = fn
            second = sn

        if first: curr.next = first



