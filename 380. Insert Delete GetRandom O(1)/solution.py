import argparse
import random


class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.random_record = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            self.random_record.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        else:
            self.set.remove(val)
            if val in self.random_record:
                self.random_record.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.random_record)


def get_argument():
    opt = argparse.ArgumentParser()
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()

    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())