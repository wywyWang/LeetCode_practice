import argparse
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        Args:
            nums (List[int]): an array of integers
            target (int): an integer

        Raises:
            NotImplementedError: No answer

        Returns:
            List[int]: indices of the array

        Thought:
            initial hash_map
            For each number:
                1. calculate rest_value
                2. if rest_value in hash_map:
                    return current index and value in the hash_map[rest_value]
                3. else:
                    add value to hash_map
            Time: O(n)
            Space: O(n)
        """
        hash_map = {}
        for index, value in enumerate(nums):
            rest_value = target - value

            if rest_value in hash_map.keys():
                return [hash_map[rest_value], index]
            else:
                hash_map[value] = index

        raise NotImplementedError


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