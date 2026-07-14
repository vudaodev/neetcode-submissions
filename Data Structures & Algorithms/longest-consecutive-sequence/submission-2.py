'''
Keep track of max_seq_len
Put all values from the set for O(1) loop up
Loop through all num within the set: 
    We are looking for the start of sequence so: 
        if (num - 1) is in the set, move onto the next num
        if (num - 1) isn't in the set, we have the start of a sequence.
    set curr_seq_len to 1 and try to find num + 1, num + 2, etc until we reach end
    of a sequence... 
    When we reach the end of a sequence, update max_seq_len
Return max_seq_len 

SC = 0(N), b/c of set
TC = ?, 0(N) to loop through each num. Inner loop would have been O(N) also
        making it O(N^2)... however, we only complete the inner loop when we have
        found the start of each sequence... Weird spot between O(N) and O(N^2)?
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, maxSeq = set(nums), 0
        for num in s:
            if (num - 1) in s: continue
            curr, seqLen = num, 0
            while curr in s:
                seqLen += 1
                curr += 1
            maxSeq = max(seqLen, maxSeq)
        return maxSeq
