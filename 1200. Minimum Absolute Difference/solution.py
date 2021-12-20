import argparse
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        Time: O(nlogn)+O(n), space: O(n)
        '''
        arr.sort()      # Timsort, O(nlogn) in the worst case.

        if len(arr) == 2:
            return [[arr[0], arr[1]]]

        total_difference = []
        min_value = 1e6

        for left in range(len(arr)-1):
            difference = arr[left+1] - arr[left]
            if difference <= min_value:
                min_value = difference
                total_difference.append((arr[left], arr[left+1], difference))

        ans = []
        for pair_1, pair_2, difference in total_difference:
            if difference == min_value:
                if pair_1 < pair_2:
                    ans.append([pair_1, pair_2])
                else:
                    ans.append([pair_2, pair_1])

        return ans


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--arr",
                        type=int,
                        nargs='+',
                        required=True,
                        help="given array")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    
    solution = Solution()

    ans = solution.minimumAbsDifference(inputs['arr'])

    print(ans)