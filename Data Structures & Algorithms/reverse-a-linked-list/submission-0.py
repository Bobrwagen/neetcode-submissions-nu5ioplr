# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        curr = head
        ne = None
        while curr.next is not None:
            ne = curr.next
            curr.next = prev
            prev = curr
            curr = ne
        curr.next = prev
        return curr

        