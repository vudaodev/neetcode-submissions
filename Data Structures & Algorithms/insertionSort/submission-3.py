# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # if value at j + 1 is smaller than value at j, then swap.
        n = len(pairs)
        res = []
        # i keeps track of the value to check in the upcoming loop.
        # when i == n == len(pairs), j == last index of the array
        # We need both an i and a j variable since:
        # the key at index (i-1) needs to be compared to all the previous keys!
        for i in range(n):
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j-=1
            res.append(pairs[:])
        return res
