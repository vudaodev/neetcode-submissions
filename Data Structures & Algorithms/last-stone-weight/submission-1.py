'''
1. Create a max heap
2. While size of heap >= 2... 
    Choose 2 heaviest stones each simulation, remove from heap
    Add (y - x) to our heap if it isn't 0
3. Return stones[0] or 0 
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) # O(n)
        while len(stones) >= 2: # Loop itself is O(n)
            y = heapq.heappop_max(stones) # O(log n) 
            x = heapq.heappop_max(stones) # O(log n)
            if x < y:
                heapq.heappush_max(stones,y-x) # O(log n)
        # Loop runs O(n) times but performs O(log n) operations inside it
        # therefore O(n) * O(log n) = O(nlogn)
        if stones: # O(1)
            return stones[0]
        return 0