class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cnt = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                cur += 1
            else:
                cnt = max(cur, cnt)
                cur = 1
        return max(cnt, cur)
