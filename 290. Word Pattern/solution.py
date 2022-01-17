import argparse
from re import L

'''
record = {}
if len(pattern) != len(s.split(' ')):
    return false

abbc dog cat cat dog
abba dog cat cat fish
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        Time: O(n), Space: O(n)
        '''
        s_list = s.split(' ')
        # edge case
        if len(pattern) != len(s_list):
            return False
        
        record_char, record_word = {}, {}
        for char, word in zip(pattern, s_list):
            if char not in record_char.keys():
                record_char[char] = word
            if word not in record_word.keys():
                record_word[word] = char
            if record_char[char] != word or record_word[word] != char:
                return False

        return True


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--pattern",
                        type=str,
                        required=True,
                        help="a pattern")
    opt.add_argument("--s",
                        type=str,
                        required=True,
                        help="a string")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.wordPattern(inputs['pattern'], inputs['s'])

    print(ans)