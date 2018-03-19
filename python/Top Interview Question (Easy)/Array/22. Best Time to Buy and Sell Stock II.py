# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#


class Solution(object):
    def maxProfit(self, prices):
        i = 0
        j = 0
        k = 0
        profit = 0
        while (k < len(prices) - 1):
            if (prices[k] < prices[k + 1]):
                j = j + 1
                k = k + 1
            else:
                profit = profit + prices[k] - prices[i]
                k = k + 1
                i = k
                j = k + 1

        profit = profit + (prices[k] - prices[i])

        return profit



if __name__ == '__main__':
    s = Solution();
    print "Hello from solution:  " + str(s.maxProfit([4, 1, 2, 3, 4, 4, 3, 7, 8, 10]))