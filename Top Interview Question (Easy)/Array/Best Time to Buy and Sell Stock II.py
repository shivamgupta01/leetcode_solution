# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
#  However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#

class Solution(object):
    def maxProfit(self, prices):
        purchasein,sellin = 0,0
        profit = 0
        if len(prices) == 0:
            return 0
        elif(sorted(prices,reverse=False) == prices):
            return prices[-1] - prices[0]
        elif(sorted(prices,reverse=True)== prices):
            return 0
        else:
            i = 0
            j = 0
            while i<len(prices)-1:
                if (profit[i]<prices[i+1]):
                    purchasein = profit[i]
                    sellin = prices[i +1]
                #     j = i + 1
                #     while(j<len(prices)-1) :
                #         if prices[j] < prices[j+1]:
                #             sellin = prices[j +1]
                #             j = j + 1
                #         else:
                #             break
                #
                #
                # profit = profit + (sellin - purchasein)
                #
                # i = j
                profit = profit + (sellin-purchasein)
                sellin = 0
                purchasein = 0
                i = i + 1
        return profit







if __name__ == '__main__':
    s = Solution()
    print "The max profit is : " + str(s.maxProfit([1,4,2]))