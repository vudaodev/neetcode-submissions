from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap of frequencies {number: count}
        counts = Counter(nums)
        # Create 'N+1' buckets for sorting
        buckets = [[] for _ in range(len(nums) + 1)]
        # Map each unique number into the bucket exactly matching its frequency
        for num, freq in counts.items():
            buckets[freq].append(num)
        # Iterate backwards starting from maximum possible frequency
        # Early return once we have found k most common
        res = []
        for i in range(len(buckets) - 1 , -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k: # If we have enough elements, return res
                    return res
        
    