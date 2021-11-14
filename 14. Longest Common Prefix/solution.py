import argparse
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        N: number of elements, L: max sequence length
        Time: O(N*L), space: O(L)
        '''
        longest_prefix = list(strs[0])

        for string in strs[1:]:
            for idx, char in enumerate(longest_prefix):
                if idx >= len(string):
                    longest_prefix = longest_prefix[:idx]
                    break
                if char != string[idx]:
                    longest_prefix = longest_prefix[:idx]
                    break

        ans = ''
        for char in longest_prefix:
            ans += char

        return ans


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--s",
                        type=str,
                        nargs='+',
                        required=True,
                        help="an array of strings")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.longestCommonPrefix(inputs['s'])

    print(ans)