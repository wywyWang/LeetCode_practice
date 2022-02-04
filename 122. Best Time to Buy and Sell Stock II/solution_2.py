'''
7 1 5 3 6 4

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Tips: Do as many one day buy/sells as we want.
        Time: O(n), space: O(1)
        '''
        ans = 0
        for i in range(1, len(prices)):
            ans += max(prices[i] - prices[i-1], 0)

        return ans