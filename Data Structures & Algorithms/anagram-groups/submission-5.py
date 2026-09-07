class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord('a') - ord(char)] += 1
            freq = tuple(freq)
            if freq not in hm:
                hm[freq] = []
            hm[freq].append(string)
        
        return list(hm.values())