class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in mp.items():
            bucket[val].append(key)
        ans = []
        for buck in range(len(bucket)-1, -1, -1):
            if bucket[buck]:
                for val in bucket[buck]:
                    ans.append(val)
                    if len(ans) == k:
                        return ans
        