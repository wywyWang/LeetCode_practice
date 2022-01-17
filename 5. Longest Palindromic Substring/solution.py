import argparse

'''
cbbd
c != b
b == b

babad
b == b

baabad
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Time: O(n^2), Space: O(2n)
        '''
        length = len(s)
        # edge case
        if length == 1:
            return s

        longest_palindrome = s[0]
        # from inner to outer
        for head in range(length):
            odd_case = self.check_palindrom(s, head, head)
            if len(odd_case) > len(longest_palindrome):
                longest_palindrome = odd_case
            even_case = self.check_palindrom(s, head, head+1)
            if len(even_case) > len(longest_palindrome):
                longest_palindrome = even_case
        return ''.join(longest_palindrome)

    def check_palindrom(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--s",
                        type=str,
                        required=True,
                        help="a string")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.longestPalindrome(inputs['s'])

    print(ans)