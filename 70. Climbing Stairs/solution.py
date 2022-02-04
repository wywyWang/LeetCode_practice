'''
2
1, 1
2

3
1, 1, 1
1, 2
2, 1

4
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        prev_n_1 = 1
        prev_n = 2
        for i in range(3, n+1):
            ans = prev_n + prev_n_1     # f(n) = f(n-1) + f(n-2)
            prev_n_1 = prev_n
            prev_n = ans
        
        return ans