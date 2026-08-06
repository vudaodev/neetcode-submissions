'''
hashmap for O(1) lookup
    Size n
Doubly Linked list to keep track of order
    Value at the head == LRU, value at the tail == Most recently used
head <-> 1 <-> 2 <-> tail
'''
class ListNode:
    def __init__(self,key = None, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node
     
            return self.hm[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value

            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev= node
        else: 
            last_node = self.tail.prev
            new_node = ListNode(key, value, last_node, self.tail)
            self.hm[key] = new_node

            last_node.next = new_node
            self.tail.prev = new_node
            
            if len(self.hm) > self.capacity:
                lru = self.head.next
                new_head = lru.next
                del self.hm[lru.key]
                self.head.next = new_head
                new_head.prev = self.head


        
