import argparse
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Time: O(logn), Space: O(n), where n = len(s)
        """
        head, tail = 0, len(s) - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--s",
                        type=str,
                        nargs='+',
                        required=True,
                        help="an array of characters")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    sol.reverseString(inputs['s'])
    print(inputs['s'])