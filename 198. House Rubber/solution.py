from typing import List

'''
2, 1, 3, 10
ans = 12
2
consider: 2+3, 2+10, 1+10
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time: O(n), Space: O(1)
        Tips: nums[1] = max(nums[0], nums[1]) and performa nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        '''
        # edge case
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return max(nums)


nums = [2, 7, 9, 3, 1]
sol = Solution()
print(sol.rob(nums))

nums = [2, 1, 3, 10]
sol = Solution()
print(sol.rob(nums))

nums = [2, 1, 3, 10, 100]
sol = Solution()
print(sol.rob(nums))