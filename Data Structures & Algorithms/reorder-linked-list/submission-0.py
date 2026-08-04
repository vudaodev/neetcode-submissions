# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Input: linked list, Output, Reordered Linked list, no return!
Ordering of the ll:
- first node in original > last node in original > second node in original > second last node in original > ...

technique:
1. Split the og LL into two (Use fast/slow to find midpoint)
2. Disconnect the two lists
3. reverse the 2nd half of the LL
4. Join the two lists

Q. does midpoint become part of left half or right half?
-> No, and it doesn't matter! 
[2    4     6      8      10]
S     F 
      S            F
            S                    F
[2,4] is first half of LL, [6,8,10] is second half of LL
We now reverse 2nd half then join
[2,   4,    6,    8]
S     F
      S           F
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle, and split list into two
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. Separate the two lists
        first = head
        second = slow.next
        slow.next = None
        # 3. Reverse the second list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev
        # 4. Join both lists:
        curr = ListNode(0)
        while first and second:
            first_t = first.next
            second_t = second.next

            curr.next = first
            curr = curr.next
            curr.next = second
            curr = curr.next

            second.next = None
            first = first_t
            second = second_t
        curr.next = first
