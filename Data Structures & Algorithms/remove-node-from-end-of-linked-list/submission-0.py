# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count+= 1
            temp = temp.next
        temp = ListNode()
        temp.next = head
        if count == n:
            return head.next
        while temp:
            if count == n:
                ne = temp.next.next
                temp.next = ne
            count -= 1
            temp = temp.next
        return head


        