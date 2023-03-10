import argparse
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_table = {}
        for index, num in enumerate(nums):
            if (target - num) in dict_table.keys():
                return [dict_table[target-num], index]
            else:
                dict_table[num] = index


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--nums",
                        type=int,
                        nargs='+',
                        required=True,
                        help="given array of integers")
    opt.add_argument("--target",
                        type=int,
                        required=True,
                        help="target integer")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    print(sol.twoSum(inputs['nums'], inputs['target']))