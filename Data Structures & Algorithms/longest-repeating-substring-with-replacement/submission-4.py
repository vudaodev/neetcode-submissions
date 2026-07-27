'''
input: 
- string s
- k, number of replacements you can make

output: 
- longest substring possible AFTER replacement

approach:
- track longest_substring globally
- Two pointer method with L and R, indicating the start and end of sub window
- For a given subwindow, longest substring possible is:
    - count of most common string + k
- While len(substring) <= most_common_count + k: move right pointer
- Everytime we move the R pointer, update longest_substring
- Move left pointer to stirng window when it gets too big
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0
        count = {}

        for R in range(len(s)):
            if s[R] not in count:
                count[s[R]] = 0
            count[s[R]] += 1
            # Length of substring CANNOT be longest than: freq of most common + k
            while (R - L + 1) > max(count.values()) + k:
                count[s[L]] -= 1
                L += 1
            # Update longest valid substring found
            longest = max(longest, R - L + 1)
        return longest
            
