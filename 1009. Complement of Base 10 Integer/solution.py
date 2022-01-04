import argparse


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        '''
        Calculate the power and use XOR
        Time: O(logn), Space: O(1)
        '''
        if n == 0:
            return 1

        power = 0
        while 2**power <= n:
            power += 1
        return n ^ (2**power-1)


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--n",
                        type=int,
                        required=True,
                        help="an integer")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    print(sol.bitwiseComplement(inputs['n']))