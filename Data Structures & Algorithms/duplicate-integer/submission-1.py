class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # mp = {}
        # for i in nums:
        #     if i in mp:
        #         mp[i] += 1
        #     else:
        #         mp[i] = 1
        # for i in mp.values():
        #     if i>1:
        #         return True
        # return False
        arr = []
        for item in nums:
            if item in arr:
                return True
            else:
                arr.append(item)
        return False