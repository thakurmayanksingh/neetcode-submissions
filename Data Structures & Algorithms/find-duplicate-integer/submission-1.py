class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for item in nums:
            if item in mp:
                return item
            else:
                mp[item] = 1