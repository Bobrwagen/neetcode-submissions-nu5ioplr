class Solution:
    def __init__(self):
        self.memo = {}
    
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If total_sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        self.memo.clear()
        return self.helper(nums, target, 0)
        
    def helper(self,nums,target,i):
        if target in self.memo:
            return self.memo[target]
        if target == 0:
            return True
        if target < 0 or i >= len(nums):
            return False
        
        include = self.helper(nums,target-nums[i],i+1)
        exclude = self.helper(nums,target,i+1)
        self.memo[target] = include or exclude
        return include or exclude

        