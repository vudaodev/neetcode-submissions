"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([_.start for _ in intervals])
        end = sorted([_.end for _ in intervals])

        s,e = 0, 0
        count, res = 0, 0

        while s < len(start):
            # If we need a room before its available:
            # increment count, and s
            if start[s] < end[e]:
                count += 1
                s += 1
            else: # room becomes available before we need it!
                count -= 1
                e += 1
            res = max(res, count)

        return res

       


