import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
                x = -heapq.heappop(heap)
                y = -heapq.heappop(heap)
                print(x,y,heap)
                if x != y:
                    heapq.heappush(heap, -abs(x-y))
                print(heap)
        return -heap[-1] if heap else 0