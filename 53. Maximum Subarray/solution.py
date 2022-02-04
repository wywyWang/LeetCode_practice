class Solution:
    def maxSubarray(nums: List[int]) -> int:
        '''
        Time: O(n), Space: O(1)
        '''
        ans = nums[0]
        current_best_sum = ans
        # edge case
        if len(nums) == 1:
            return ans

        for i in range(1, len(nums)):
            current_best_sum = max(current_best_sum+nums[i], nums[i])
            ans = max(ans, current_best_sum)

        return ans