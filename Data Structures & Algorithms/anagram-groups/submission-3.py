class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a hashmap and the timsort function: 
            # key: sorted string in alphabetical order -> 'act'
            # Value: a list of all strings that become the given key when sorted
            # ['act','cat']
            # T/C: O(n* m log m), where m is the average char length, n is number of strings
            # S/C: O(n*m)
        # Use a hashmap with the key being a tuple with frequency count of each character
            # key: tuple with the freq count of each character 
            # Value: list of all strings that satisfies the condition of the key
            # T/C: O(n*m)
            # S/C: O(n*m)
        hm = {}
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            if count not in hm:
                hm[count] = []
            hm[count].append(string)
        return [subarray for subarray in hm.values()]

        