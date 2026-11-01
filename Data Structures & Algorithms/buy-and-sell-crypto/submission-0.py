class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1
        maxProfit = 0
        n = len(prices)
        while j<n:
            if prices[j] < prices[i]:
                i = j
            else:
                curProfit = prices[j] - prices[i]
                maxProfit = max(maxProfit, curProfit)
            j += 1
        return maxProfit