import argparse
from typing import List


'''
if row == col:
    record[row][col] = max(1, record[row-1][col], record[row][col-1])
else:
    if nums[row] < nums[col]:
        record[row][col] = max(record[row-1][col], record[row][col-1]+1)
    # else:
    #     record[row][col] = max(record[row-1][col], record[row][col-1])

        1   2   0   5   6
    0   0   0   0   0   0
1   0   1   2   1   2   2
2   0   x   x   1   2   3
0   0   x   x   1   2   3
5   0   x   x   x   1   2
6   0   x   x   x   x   5

1   2   0   5   6
0   0   0   0   0


'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)

        # edge case
        if length == 0:
            return 0

        record_LIS = [0 for row in range(length)]

        for row in range(length):
            max_lis = 0
            for col in range(row-1, -1, -1):
                if nums[col] < nums[row]:
                    max_lis = max(max_lis, record_LIS[col])
            record_LIS[row] = max_lis+1
        
        return max(record_LIS)


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--nums",
                        type=int,
                        nargs='+',
                        required=True,
                        help="an integer array")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.lengthOfLIS(inputs['nums'])

    print(ans)