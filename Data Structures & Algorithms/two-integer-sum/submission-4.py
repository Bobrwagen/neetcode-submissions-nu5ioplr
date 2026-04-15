class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            td = target - num
            if td in diff:
                return [diff[td], i]
            else:
                diff[num] = i
        return None