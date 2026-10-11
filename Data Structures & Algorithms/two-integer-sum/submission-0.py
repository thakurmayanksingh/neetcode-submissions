class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, item in enumerate(nums):
            comp = target-item
            if comp in mp:
                ans = [idx, mp[comp]]
                break
            mp[item] = idx
        return sorted(ans)