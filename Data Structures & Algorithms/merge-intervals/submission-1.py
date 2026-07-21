'''
Input: list of intervals
Output: list of non overlapping intervals

Method:
- Create a list for us to return (res)
- Sort intervals based on start value O(n log n)
- Loop through all intervals:
    - If res is empty, or curr_interval start doesn't overlap w/
        prev interval, append curr_interval to res. 
    - Else, change prev interval end (largest of curr/prev interval end)

interval i and i+1 overlap if:
i_end >= i+1_start

'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        res = []
        for interval in intervals:
            # prev internal is res[-1]
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
