import argparse
import itertools


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = [combination for combination in itertools.combinations(characters, combinationLength)]
        self.current_idx = 0

    def next(self) -> str:
        ans = ''.join(self.combinations[self.current_idx])
        self.current_idx += 1
        return ans

    def hasNext(self) -> bool:
        if self.current_idx + 1 <= len(self.combinations):
            return True
        else:
            return False


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--characters",
                        type=str,
                        required=True,
                        help="a string")
    opt.add_argument("--combinationLength",
                        type=int,
                        required=True,
                        help="a number of combination length")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()

    obj = CombinationIterator(inputs['characters'], inputs['combinationLength'])
    
    actions = ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    for action in actions:
        if action == 'CombinationIterator':
            print(None)
        elif action == 'next':
            print(obj.next())
        elif action == 'hasNext':
            print(obj.hasNext())