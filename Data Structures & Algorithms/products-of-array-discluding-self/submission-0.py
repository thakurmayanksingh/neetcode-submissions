class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prefix = 1
        n = len(nums)
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans