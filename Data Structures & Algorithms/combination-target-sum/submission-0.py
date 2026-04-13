class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        combs = set()
        def dp(cur,ind):
            if ind >= n:
                return
            if sum(cur) > target:
                return
            # add num
            if sum(cur) == target:
                combs.add(cur)
                return
            dp(cur, ind + 1)
            cur = cur + (nums[ind],)
            dp(cur, ind)
        dp(tuple(), 0)
        return [list(c) for c in combs]
        