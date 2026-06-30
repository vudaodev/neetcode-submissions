class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = []
        for c in s:
            if c.isalnum():
                cleaned_chars.append(c.lower())
        cleaned_s = "".join(cleaned_chars)
        reversed_s = cleaned_s[::-1]
        return cleaned_s == reversed_s