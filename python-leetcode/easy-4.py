"""
Say you have an array for which the ith element
is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

The key point is we need to consider every peak immediately
following a valley to maximize the profit.
In case we skip one of the peaks (trying to obtain more profit),
we will end up losing the profit over one of the transactions
leading to an overall lesser profit.
"""

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        end = len(prices) - 1

        while i < end:

            # find valley
            # \_ or \/
            # continue going down, until price goes up/same
            while i < end and prices[i] >= prices[i + 1]:
                i+=1

            valley = prices[i]

            # find peak
            # /- or /\
            # continue going up, until price goes down/same
            while i < end and prices[i] <= prices[i + 1]:
                i+=1

            peak = prices[i]

            # add profit
            max_profit += peak - valley

        return max_profit


class Solution2:
    # We can crawl over the the slop keep on
    # add ing the profit obtained from
    # every consecutive transaction
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i]

        return max_profit




