import argparse
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # method 1
        # '''
        # Time: O(n), Space: O(n)
        # '''
        # if not head:
        #     return None

        # reversed_linked_list = ListNode(head.val)
        # head = head.next
        # while head:
        #     reversed_linked_list = ListNode(head.val, reversed_linked_list)
        #     head = head.next
        # return reversed_linked_list

        # method 2
        '''
        Time: O(n), Space: O(1)
        '''
        previous, current = None, head
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        return previous


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--head",
                        type=int,
                        nargs='+',
                        required=False,
                        help="the head of a singly linked list")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    
    solution = Solution()

    ans = solution.reverseList(inputs['arr'])
    print(ans)