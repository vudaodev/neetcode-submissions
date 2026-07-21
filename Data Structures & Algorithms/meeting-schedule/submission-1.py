"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
1. Sort intervals in ascending order, according to start times
2. Loop through all intervals
    If an interval overlaps, return False
    We know that an interval i overlaps the prev if:
    i_start < i-1_end
    Note that if i-1_end == i_start, this is NOT overlapping
3. Return True if we reach the end
T/C: O(nlogn) sorting, O(n) iterating, O(nlogn) overall
S/C: O(1) 
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda _: _.start)
        for i in range(1,len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True