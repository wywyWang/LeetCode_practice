import argparse
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Given two sorted arrays nums1 and nums2 of size m and n respectively, 
        return the median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
        '''
        
        # Solution 1
        merged_array = []
        median_index = (len(nums1) + len(nums2)) // 2

        ## edge case
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return sum(nums2[median_index-1:median_index+1]) / 2        # even: (index + last_index) / 2
            else:
                return nums2[median_index]                                  # odd: index
        elif len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return sum(nums1[median_index-1:median_index+1]) / 2        # even: (index + last_index) / 2
            else:
                return nums1[median_index]                                  # odd: index

        ## normal case
        nums1_index, nums2_index = 0, 0
        while (nums1_index + nums2_index) <= median_index:
            if nums2_index >= len(nums2) or nums1_index < len(nums1) and nums1[nums1_index] <= nums2[nums2_index]:
                merged_array.append(nums1[nums1_index])
                nums1_index += 1
            else:
                merged_array.append(nums2[nums2_index])
                nums2_index += 1
        
        if (len(nums1) + len(nums2)) % 2 == 0:
            return sum(merged_array[-2:]) / 2       # even: (index + last_index) / 2
        else:
            return merged_array[median_index]       # odd: index


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--nums1",
                        type=int,
                        default=[],
                        nargs='+',
                        required=False,
                        help="sorted array 1")
    opt.add_argument("--nums2",
                        type=int,
                        default=[],
                        nargs='+',
                        required=False,
                        help="sorted array 2")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.findMedianSortedArrays(inputs['nums1'], inputs['nums2'])

    print(ans)