class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0]*self.capacity 
        self.length = 0 


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # Resize if at capacity
        if self.length == self.capacity:
            self.resize()
        
        self.array[self.length] = n
        self.length += 1
        

    def popback(self) -> int:
        res = self.array[self.length - 1]
        self.length -= 1
        return res

    def resize(self) -> None:
        # Create new Arr
        self.array = self.array + [0]*self.capacity
        # Increase Capacity
        self.capacity*=2
    

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity