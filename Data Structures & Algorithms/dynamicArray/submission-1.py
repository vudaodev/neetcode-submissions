class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Resize if at capacity:
        if self.size == self.capacity:
            self.resize()
        # Insert at next empty index:
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # I used a temp variable, but you can just 'soft delete'
        if self.size > 0:
            temp = self.arr[self.size - 1]
            self.arr[self.size - 1] = 0
            self.size -= 1
        return temp
        # if self.size > 0:
        #     self.size -= 1
        # return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        temp_arr = [0]*self.capacity
        for i in range(self.size):
            temp_arr[i] = self.arr[i]
        self.arr = temp_arr  

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
