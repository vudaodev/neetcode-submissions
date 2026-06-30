class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# self.head <-> node1 <-> node 2 <-> self.tail
class Deque:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        # if self.head.next = self.tail:
        #     return True
        # return False
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last_node = self.tail.prev
        prev_node = last_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        return last_node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.val
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
        
