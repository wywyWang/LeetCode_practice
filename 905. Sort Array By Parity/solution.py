import argparse
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        Time: O(n), Space: O(n)
        '''
        odd_array, even_array = [], []
        for num in nums:
            if num % 2 == 0:
                even_array.append(num)
            else:
                odd_array.append(num)
        return even_array + odd_array


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

    ans = solution.sortArrayByParity(inputs['arr'])
    print(ans)