class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
                0
        if len(nums) == 1:
            return nums[0]
        dp_1 = nums[1:]
        dp_2 = nums[:-1]
        def dp(arr):
            rob1, rob2 = 0, 0

            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(dp(dp_1), dp(dp_2))
            
        