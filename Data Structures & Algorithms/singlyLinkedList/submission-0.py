class ListNode:
    def __init__(self, val = None , next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Dummy Variable
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next # Points to the head?
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1 # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) # Create a new Node
        new_node.next = self.head.next # Point new Node to the old head
        self.head.next = new_node # Point the head to new node
        if not new_node.next: # If there is no other value:
            self.tail = new_node # = self.head works too?

    def insertTail(self, val: int) -> None:
        # new_node = ListNode(val) # Create a new node.
        # self.tail.next = new_node # Change pointer of the old tail from None.
        self.tail.next = ListNode(val)
        self.tail = self.tail.next # Our new node becomes the tail. 

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        # Stops running when i == index
        while i < index and current:
            i += 1
            current = current.next
        ## The following code runs once i == index:
        # current.next exists, which means index is in-bound:
        if current and current.next:
            # If next node is the tail
            if current.next == self.tail:
                self.tail = current
            # If next node is not the tail
            current.next = current.next.next
            return True
        # Index is out of bounds:
        return False
        
    def getValues(self) -> List[int]:
        current = self.head.next
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res


        
