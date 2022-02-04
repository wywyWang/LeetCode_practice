class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time: O(n), Space: O(1)
        '''
        ans = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            # smaller -> buy
            if prices[i] < buy:
                buy = prices[i]
            else:
                # larger profit -> sell
                ans = max(ans, prices[i] - buy)

        return ans