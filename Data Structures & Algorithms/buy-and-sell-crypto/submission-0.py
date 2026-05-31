class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the biggest delta between two numbers
        # no limit on the spacing between?

        # is there a better solution than n^2 ? or maybe its n logn?
        # iterate over each number... 

        # maybe you iterate over each number and then look forward to the best day / end of the list... i feeel like thats not O(n) ???

        l, r = 0, 1

        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
