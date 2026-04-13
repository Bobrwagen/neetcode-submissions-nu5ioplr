class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])
        return min(cost[0] + self.minCostClimbingStairs(cost[1:]), cost[1] + self.minCostClimbingStairs(cost[2:])) 