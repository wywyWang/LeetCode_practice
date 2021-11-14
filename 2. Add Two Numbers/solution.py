import argparse
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, l):
        self.root = None
        self.construct_linked(l)

    def construct_linked(self, l):
        for value in l:
            if self.root is None:
                self.root = ListNode(value)
            else:
                self._insert(self.root, value)

    def _insert(self, current_node, value):
        if current_node.next is None:
            current_node.next = ListNode(value)
        else:
            self._insert(current_node.next, value)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Space: O(n), time: O(M)
        '''

        answer = l1
        overflow = 0

        while 1:
            if l2 is None:
                while overflow:
                    l1.val += 1
                    if l1.val // 10 == 1:
                        overflow = 1
                        l1.val %= 10
                    else:
                        overflow = 0
                    
                    if overflow and l1.next is None:
                        l1.next = ListNode(0)
                    l1 = l1.next

                break

            l1.val = l1.val + l2.val + overflow
            if l1.val // 10 == 1:
                overflow = 1
                l1.val %= 10
            else:
                overflow = 0
            
            if l1.next is None and l2.next is not None or l1.next is None and overflow:
                l1.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next

        return answer


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--l1",
                        type=int,
                        nargs='+',
                        required=True,
                        help="linked list 1 in reverse order")
    opt.add_argument("--l2",
                        type=int,
                        nargs='+',
                        required=True,
                        help="linked list 2 in reverse order")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    
    # construct linked list
    l1 = LinkedList(inputs['l1'])
    l2 = LinkedList(inputs['l2'])

    ans = sol.addTwoNumbers(l1.root, l2.root)

    # test the result
    while 1:
        print(ans.val, sep=', ')
        if ans.next is None:
            break
        else:
            ans = ans.next