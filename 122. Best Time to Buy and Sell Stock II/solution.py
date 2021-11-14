import argparse
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Tips: Do as many one day buy/sells as we want.
        Time complexity: O(n), space: O(1)
        '''
        ans = 0
        for i in range(1, len(prices)):
            ans += max(prices[i]-prices[i-1], 0)
        return ans


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--prices",
                        type=int,
                        nargs='+',
                        required=True,
                        help="prices of a given stocks")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.maxProfit(inputs['prices'])

    print(ans)