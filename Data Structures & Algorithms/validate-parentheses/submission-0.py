class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        d = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in d:
                if len(ans)>0 and ans[-1]==d[ch]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(ch)
        if len(ans)>0:
            return False
        return True