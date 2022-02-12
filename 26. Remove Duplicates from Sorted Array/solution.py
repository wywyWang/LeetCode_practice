from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Time: O(n), Space: O(1)
        '''
        # edge case
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        appeared = None
        index = 0
        while index < len(nums):
            if appeared is None:
                appeared = nums[index]
                index += 1
            elif nums[index] == appeared:
                del nums[index]
            else:
                appeared = nums[index]
                index += 1

        return len(nums)