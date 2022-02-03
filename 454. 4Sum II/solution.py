from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        '''
        Time: O(n^2), Space: O(n^2)
        '''
        
        ans = 0
        possible_sum = {}

        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 not in possible_sum.keys():
                    possible_sum[num1+num2] = 1
                else:
                    possible_sum[num1+num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in possible_sum.keys():
                    ans += possible_sum[-(num3+num4)]
        return ans