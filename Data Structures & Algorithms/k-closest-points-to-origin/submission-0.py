import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make heap
        print(points)
        def dist(x1, x2):
            length = x1 * x1 + x2 * x2
            return (length, x1, x2)
        trips = [dist(x1,x2) for x1,x2 in points]
        print(trips)
        heapq.heapify(trips)
        print(trips)
        res = []
        for _ in range(k):
            _,x1,x2 = heapq.heappop(trips)
            res.append([x1,x2])
        return res