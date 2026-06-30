class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # Dummy head
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i, curr = 0, self.head.next
        # does while i <= index work?
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val,self.head.next)
        self.head.next = new_node
        # Edge case, list was empty before insertion:
        if new_node.next == None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i, prev, curr = 0, self.head, self.head.next
        while curr and i <= index:
            if i == index:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next                    
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
