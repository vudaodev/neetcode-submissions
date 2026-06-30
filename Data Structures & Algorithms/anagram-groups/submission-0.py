class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for string in strs:
            # Find frequency count for string
            freq = [0]*26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            # Change freq to tuple:
            freq = tuple(freq)
            # Create an empty list if we haven't a word with this freq before
            if freq not in hm:
                hm[freq] = []
            # Add string to our hashmap
            hm[freq].append(string)
        
        return [hm[_] for _ in hm]