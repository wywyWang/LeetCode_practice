import argparse
from asyncio.windows_events import NULL
from copy import deepcopy
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time: O(n); n is the length of the first reaching cycle. Space: O(1)
        '''
        # edge case
        if not head:
            return None
        if not head.next:
            return None

        while head:
            # set the value as the number out of tha range to check if cycle.
            if head.val == (1e5 + 1):
                return head
            head.val = 1e5 + 1
            head = head.next

        # no cycle
        return None