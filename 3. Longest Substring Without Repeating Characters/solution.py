import argparse


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Tips: Use dictionary to perform sliding window. The dictionary will only keep the latest key
        Time complexity: O(n), space complexity: O(n)
        '''

        # edge case
        if len(s) < 2:
            return len(s)

        left = 0
        record = {s[left]: left}
        ans = 0
        for right in range(1, len(s)):
            if s[right] in record:
                left = max(left, record[s[right]]+1)        # next of the appeared one

            record[s[right]] = right                        # update automatically if duplicate
            ans = max(ans, right-left+1)
            
        return ans


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

    ans = sol.lengthOfLongestSubstring(inputs['s'])

    print(ans)