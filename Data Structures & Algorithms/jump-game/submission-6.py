class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        jumps,curr = nums[0],0
        while jumps > 0 and curr < len(nums) -1 :
            if curr + jumps >= len(nums):
                return True
            currMax = nums[curr]
            currInd = curr
            for i in range(curr + 1, min(curr+jumps+1,len(nums))):
                if nums[i] + i >= currMax + currInd:
                    currMax = nums[i]
                    currInd = i
            jumps = currMax
            curr = currInd
            print(f'{jumps} and {curr}')
        return curr == len(nums)-1