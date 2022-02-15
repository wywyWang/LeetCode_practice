from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        Time: O(n), Space: O(1)
        '''
        if len(digits) == 0:
            raise NotImplementedError

        index = len(digits) - 1
        digits[index] += 1
        while digits[index] == 10:
            digits[index] = 0
            if index != 0:
                digits[index-1] += 1
            else:
                digits = [1] + digits
                break
            index -= 1

        return digits