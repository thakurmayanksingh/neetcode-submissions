class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        i = 1
        while i<len(s):
            score += abs(ord(s[i-1]) - ord(s[i]))
            i += 1
        return score