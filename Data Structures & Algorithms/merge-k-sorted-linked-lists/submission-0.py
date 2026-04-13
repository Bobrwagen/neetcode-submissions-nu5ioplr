# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        k = len(lists)
        ptrs = [None] * k
        #init
        for i in range(k):
            ptrs[i] = lists[i]
            heapq.heappush(heap, ptrs[i].val)
        head = None
        cur = None
        while len(heap) > 0:
            n = heapq.heappop(heap)
            # find ptr
            for i in range(k):
                if ptrs[i] and ptrs[i].val == n:
                    if head is None:
                        cur = ptrs[i]
                        head = cur
                    # tmp = p.next
                    else:
                        cur.next = ptrs[i]
                        cur = cur.next
                    ptrs[i] = ptrs[i].next
                    if ptrs[i]:
                        heapq.heappush(heap,ptrs[i].val)
        return head




        