class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings cannot be anagrams of each other if they are of different lengths
        if len(s) != len(t):
            return False
        # Create an array to count frequencies
        freqCount = [0]*26
        # Add to frequency count for characters in s
        for _ in s:
            freqCount[ord(_) - ord('a')] += 1
        # Take away from frequency count for characters in T
        for _ in t:
            freqCount[ord(_) - ord('a')] -= 1
        # Empty freqCount means we have a valid anagram (s and t cancel out)
        return freqCount == [0]*26;

