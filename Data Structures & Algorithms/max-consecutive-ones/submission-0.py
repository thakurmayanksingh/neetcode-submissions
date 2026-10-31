class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = temp_counter = 0
        for num in nums:
            if num == 1:
                temp_counter += 1
            else:
                res = max(temp_counter, res)
                temp_counter = 0
        return max(res, temp_counter)