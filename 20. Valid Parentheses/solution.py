import argparse


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time: O(n), Space: O(n)
        '''
        parentheses = {'(': ')', '[': ']', '{': '}'}
        appeared_list = []
        for char in s:
            if char in parentheses.keys():
                appeared_list.append(parentheses[char])
            else:
                if len(appeared_list) == 0:
                    return False
                elif char == appeared_list.pop():
                    pass
                else:
                    return False
        
        if len(appeared_list) == 0:
            return True
        else:
            return False


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--s",
                        type=str,
                        required=True,
                        help="a parentheses string")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    print(sol.isValid(inputs['s']))