# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        n = len(pairs)
        # Sort the first element, then the first 2 etc, until n-1.
        # Swap if key at j < key at j - 1
        for i in range(n):
            j = i
            while j >= 1 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j-1], pairs[j]
                j-= 1
            res.append(pairs[:])
        return res

