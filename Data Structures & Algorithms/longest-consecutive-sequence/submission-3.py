'''
Input: nums array
Output: longest consecutive seq length

track: LCS (Longest consecutive sequence)

Naive approach: Sort then use two pointer to find LCS. 
- T/C: O(nlogn) due to timsort, S/C: O(1)

Optimised approach: HashSet for O(1) lookups
- T/C: O(n), S/C: O(n)
- Create a hashset, and a variable to track LCS
- Go through all num in nums:
    - Aim to find the 'start' of sequences
    - If a num isn't the start of a sequence, move on
    - If num is the start of a sequence, find out how long the sequence is
        by doing lookups in the HS
    - Update LCS accordingly
- Return LCS
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        lcs = 0
        for num in nums:
            if (num - 1) in hs: continue
            curr,count = num, 0 # set curr to start of seq
            while curr in hs: 
                count += 1 # update seq length
                curr += 1 # update current number
            lcs = max(lcs, count)
        return lcs