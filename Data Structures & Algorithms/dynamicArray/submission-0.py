class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Resize if at capacity:
        if self.length == self.capacity:
            self.resize()
        # Insert at next empty index:
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # I used a temp variable, but you can just 'soft delete'
        # if self.length > 0:
        #     temp = self.arr[self.length]
        #     self.arr[self.length] = 0
        #     self.length -= 1
        #     return temp
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]
        # Neet has it as self.length instead of self.length + 1
        # Are we returning the popped element or the new end of array?
    def resize(self) -> None:
        self.capacity *= 2
        tempArr = [0]*self.capacity
        for i in range(self.length):
            tempArr[i] = self.arr[i]
        self.arr = tempArr  

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
