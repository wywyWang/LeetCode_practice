import argparse


class Solution:
    def __init__(self) -> None:
        self.roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        '''
        Note: 
        1. I can be placed before V and X
        2. X can be placed before L and C
        3. C can be placed before D and M
        '''
        
        possible_before_table = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        index = 0
        ans = 0
        while index < len(s):
            if s[index] in possible_before_table.keys():
                if index == len(s) - 1:                 # edge case
                    ans += self.roman_table[s[index]]
                    index += 1
                else:
                    if s[index+1] in possible_before_table[s[index]]:
                        ans -= self.roman_table[s[index]]
                        ans += self.roman_table[s[index+1]]
                        index += 2
                    else:
                        ans += self.roman_table[s[index]]
                        index += 1
            else:
                ans += self.roman_table[s[index]]
                index += 1

        return ans


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--s",
                        type=str,
                        required=True,
                        help="roman numeral")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.romanToInt(inputs['s'])

    print(ans)