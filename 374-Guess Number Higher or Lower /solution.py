import argparse


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(guess_num: int) -> int:
    if pick < guess_num:
        return -1
    elif pick > guess_num:
        return 1
    elif pick == guess_num:
        return 0
    else:
        raise NotImplementedError


class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        Use binary search, space: O(1), time: O(log_2n)
        '''
        return self._guess(1, n)
    
    def _guess(self, low_range: int, high_range: int) -> int:
        answer = (high_range+low_range) // 2
        guess_flag = guess(answer)
        if guess_flag == -1:
            return self._guess(low_range, answer-1)
        elif guess_flag == 1:
            return self._guess(answer+1, high_range)
        elif guess_flag == 0:
            return answer
        else:
            raise NotImplementedError


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--n",
                        type=int,
                        required=True,
                        help="max number")
    opt.add_argument("--pick",
                        type=int,
                        required=True,
                        help="picked number to be guessed")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    global pick
    pick = inputs['pick']
    print(sol.guessNumber(inputs['n']))