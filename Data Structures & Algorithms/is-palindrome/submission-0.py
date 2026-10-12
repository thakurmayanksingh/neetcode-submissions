class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for char in s.lower():
            if char.isalnum():
                ans += char
        return True if ans == ans[::-1] else False