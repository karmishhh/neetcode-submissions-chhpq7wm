# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next: # we check both fast and fast.next as not null since if fast exist then we can say that it can point to null, but null cannot point to null. 
        # similarly we are also doing fast.next.next so for it to happen, we should make sure that fast.next exists
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False