"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Input: array of intervals
Output/ Solve: max_count, What is the maximum amount of rooms we need at once

i_end == i+1_start => not a conflict
i_end > i+1_start => conflict

Create two arrays: start and end 
Two pointer technique with S/E

Loop through all start values and ask ourselves:
- Has a room been made available before we need it?
- If not: Increase count, move S pointer
- If yes: Decrement count, move E pointer

- Return max_count
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        s,e = 0, 0
        count, max_count = 0,0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            max_count = max(max_count, count)
        
        return max_count

        