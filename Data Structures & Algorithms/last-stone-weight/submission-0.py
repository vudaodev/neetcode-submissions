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
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            if x < y:
                heapq.heappush_max(stones,y-x)
        if stones:
            return stones[0]
        return 0