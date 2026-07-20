'''
T/C if using timsort: n words, words are m length -> O(n*m log m) 

Use hm and to keep track of group anagrams
Key of hm: char freq count
values of hm: array with all strings that follow char freq count
T/C: O(n*m) -> You have to loop through n words and m chars to find freq count
S/C: O(n*m)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for string in strs:
            freq_count = [0]*26
            for char in string:
                freq_count[ord(char) - ord('a')] += 1
            freq_count = tuple(freq_count)
            if freq_count not in hm:
                hm[freq_count] = []
            hm[freq_count].append(string)
        return [_ for _ in hm.values()]