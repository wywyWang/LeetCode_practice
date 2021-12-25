import argparse


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        previous_operation = '+' # default is plus but doing stack, will plus in the end

        for index, number in enumerate(s):
            # transform strings to number
            if number.isnumeric():
                num = num * 10 + int(number)
            if number in '+-*/' or index == len(s) - 1:
                if previous_operation == '+':
                    stack.append(num)
                elif previous_operation == '-':
                    stack.append(-num)
                elif previous_operation == '*':
                    operated_num = stack.pop() * num
                    stack.append(operated_num)
                elif previous_operation == '/':
                    operated_num = int(stack.pop() / num)
                    stack.append(operated_num)
                else:
                    raise NotImplementedError
            
                previous_operation = number
                num = 0
        
        return sum(stack)
        

def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--s",
                        type=str,
                        required=True,
                        help="representation an expression")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    print(sol.calculate(inputs['s']))