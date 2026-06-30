class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Initialise with a dummy variable. 
        # Dummy variable.next points to the actual head
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr and i <= index:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        # Create new node:
        new_node = ListNode(val)
        new_node.next = self.head.next
        # If list was previously empty:
        if not self.head.next:
            self.tail = new_node
        # Set new Head:
        self.head.next = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        # Set old tail to point to new node:
        self.tail.next = new_node
        # Set new tail:
        self.tail = new_node

    def remove(self, index: int) -> bool:
        # Think about what happens if we are removing the head or tail.
        i = 0
        prev = self.head
        curr = self.head.next
        while curr and i <= index:
            if i == index:
                if curr == self.tail:
                    self.tail = prev
                # We don't need to do the same check for head
                # because of the line below
                prev.next = curr.next
                return True
            i += 1
            prev = prev.next
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        i = 0
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
        
