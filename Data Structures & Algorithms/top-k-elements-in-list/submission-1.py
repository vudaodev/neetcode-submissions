class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use hm/dict to keep track of the frequency counts of each number -> O(n)
        # Sort the hm/dict in desc order based on frequency count -> timsort (Onlogn)
            # sorted() -> list of tuples that contain k,v pairs
        # Return the top k most common elements

        # t/c = O(nlogn), s/c = O(n)

        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        # list that contains (key,value) tuples
        sorted_list = sorted(hm.items(), key = lambda _ : _[1], reverse = True)
        # Return the top k most common
        res = []
        for i in range(k):
            res.append(sorted_list[i][0])
        return res