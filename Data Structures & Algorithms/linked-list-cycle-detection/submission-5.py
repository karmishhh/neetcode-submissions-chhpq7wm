# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = defaultdict(int)
        curr = head
        while curr:
            hashmap[curr] += 1
            if hashmap[curr] > 1:
                return True
            curr = curr.next
        return False

        