
# singly linked list - none -> 1 -> 2 -> 3 -> 4 -> null 
# reverse singly linked list -  null< -1 <- 2 <- 3 <- 4 <- none


# # In the context of linked lists, head, prev, curr, and tail (if you were using one) are all pointers (or references) to nodes within the linked list.

# head: A pointer to the very first node of the list. It's the entry point to the entire data structure.

# prev: A pointer that typically keeps track of the node before the current node you're processing.

# curr: A pointer that points to the current node being examined or manipulated.

# tail: A pointer to the very last node of the list (though not always explicitly used or maintained in every linked list implementation).


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        head = prev
        return head
        