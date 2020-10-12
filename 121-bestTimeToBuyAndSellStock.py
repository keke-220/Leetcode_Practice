class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_price = 0
        prev_ans = max_price - min_price
        
        if len(prices) == 0:
            return 0
        
        for price in prices:
            if price < min_price:
                min_price = price
                max_price = 0
            if price > max_price:
                max_price = price
            ans = max_price - min_price
            if prev_ans <= ans:
                prev_ans = ans

        if prev_ans < 0:
            return 0
        else: return prev_ans
