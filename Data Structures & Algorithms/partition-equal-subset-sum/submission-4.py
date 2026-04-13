class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i, left, right):
            if i >= len(nums):
                if left == []:
                    return False
                return sum(left) == sum(right)
            skip = dp(i+1,left[:],right[:])
            left.append(nums[i])
            right.remove(nums[i])
            take = dp(i+1, left[:], right[:])
            return skip or take
        return dp(0,[],nums[:])      