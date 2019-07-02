'''
Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete
at most one transaction (i.e., buy one and sell
one share of the stock), design an algorithm
to find the maximum profit.

Note that you cannot sell a stock before you buy one.

The points of interest are the peaks and valleys in the given graph.
We need to find the largest peak following the smallest valley.
We can maintain two variables - minprice and maxprofit
corresponding to the smallest valley and maximum profit
(maximum difference between selling price and minprice)
obtained so far respectively.
'''

class Solution1:
    # brute force
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                current = prices[j] - prices[i]
                if current > profit:
                    profit = current

        return profit


class Solution2:
    # As you pass through the prices
    # update the smallest price encountered
    # as you encounter a new price, check if
    # the profit made given the smallest encounted price
    # so far and the current encountered price
    # has a larger profit than the current known maximum profit
    # if so, this is the current known maximum profit
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        minprice = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit


