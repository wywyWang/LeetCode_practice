import argparse
import math

'''
x: 123

reversed_x: 3, x: 12
reversed_x: 32, x: 1
reversed_x: 321, x: 0
'''


class Solution:
    def reverse(self, x: int) -> int:
        '''
        Time: O(n), Space: O(1)
        '''

        # edge case
        if x == 0:
            return 0

        negative = False
        if x < 0:
            negative = True
            x = -x
        reversed_x = 0
        while x != 0:
            reversed_x *= 10
            reversed_x += (x % 10)
            x = x // 10
        
        if negative:
            reversed_x = -reversed_x
            if reversed_x < -2 ** 31:
                return 0
        else:
            if reversed_x > 2 ** 31 - 1:
                return 0

        return reversed_x


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--x",
                        type=int,
                        required=True,
                        help="a signed integer")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.reverse(inputs['x'])

    print(ans)