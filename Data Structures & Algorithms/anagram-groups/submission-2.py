class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m = average string length, n = number of strings
        # Solution 1: sort the strings -> TC: (m log m) * n 
        # Solution 2: look at frequency count of characters -> TC: m*n
        # O(n*m) space for either solution

        hm = {}

        for string in strs:
            freq = [0]*26
            # Updated freq count:
            for char in string:
                freq[ord(char) - ord('a')] += 1
            # Add freq count / word to hashmap:
            freq_tuple = tuple(freq)
            if freq_tuple not in hm:
                hm[freq_tuple] = []
            hm[freq_tuple].append(string) #check syntax

        return [_ for _ in hm.values()]

