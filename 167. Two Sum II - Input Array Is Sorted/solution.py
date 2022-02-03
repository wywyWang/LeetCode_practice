from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Time: O(n), Space: O(1)
        '''
        length = len(numbers)
        # edge case
        if length == 0:
            raise NotImplementedError

        left, right = 0, length - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] <= target:
                left += 1
            else:
                right -= 1


# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         '''
#         Time: O(nlogn), Space: O(n)
#         '''
#         length = len(numbers)
#         # edge case
#         if length == 0:
#             return NotImplementedError

#         self.numbers = numbers

#         for index in range(length):
#             find = self.binary_search(index+1, length-1, target-numbers[index])
#             if find != -1:
#                 return [index+1, find+1]

#         # edge case
#         return NotImplementedError

#     def binary_search(self, left: int, right: int, match: int) -> int:
#         find = -1
#         if left > right:
#             return find

#         middle = (right-left+1) // 2 + left
#         if self.numbers[middle] == match:
#             return middle
#         # reach edge
#         if left == right:
#             return find
#         if self.numbers[middle] <= match:
#             find = self.binary_search(middle+1, right, match)
#         elif self.numbers[middle] > match:
#             find = self.binary_search(left, middle-1, match)

#         return find