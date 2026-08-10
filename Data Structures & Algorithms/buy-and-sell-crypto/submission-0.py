class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Store the curr lowest, the curr max, and the biggest difference
        l = prices[0]
        m = 0
        for i in prices:
            l = min(i,l)
            m = max(m, i - l)
        return m
