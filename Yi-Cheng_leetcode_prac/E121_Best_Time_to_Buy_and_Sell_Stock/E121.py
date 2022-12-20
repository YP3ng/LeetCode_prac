class Solution:
    def maxProfit(self, prices):

        res = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                res = max(res, prices[right] - prices[left])
                right += 1
        return res