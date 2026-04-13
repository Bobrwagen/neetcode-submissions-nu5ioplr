class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in targets:
                return [targets[diff], i]
            else:
                targets[nums[i]] = i
        return []