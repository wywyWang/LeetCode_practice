from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []

        # edge case
        if len(s) == 0:
            return ans
        elif len(s) == 1:
            return [1]
        
        def map_left_and_right_indices(s_part: List[str], char: str):
            left, right = 1e3, -1
            for index, c in enumerate(s_part):
                if c == char:
                    if index < left:
                        left = index
                    if index > right:
                        right = index
            return left, right
        
        # find the interval of each char
        char_mapping, char_record = {}, set()
        for index, char in enumerate(s):
            if char in char_record:
                continue
            char_record.add(char)
            left_position, right_position = map_left_and_right_indices(s[index:], char)
            char_mapping[char] = [left_position+index, right_position+index]

        # find interval
        left_part, right_part = 0, 0
        for char in char_mapping.keys():
            left_position, right_position = char_mapping[char]
            if left_position == left_part:
                right_part = right_position
                continue

            if left_position > right_part:
                ans.append(right_part-left_part+1)
                left_part = left_position
                right_part = right_position
            elif right_position > right_part:
                right_part = right_position

        ans.append(right_part-left_part+1)
        return ans


solution = Solution()
s = "eccbbbbdec"
print(solution.partitionLabels(s))

s = "ababcbacadefegdehijhklij"
print(solution.partitionLabels(s))