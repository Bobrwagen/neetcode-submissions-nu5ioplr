class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dp(i, cur):
            print(i,cur)
            if i >= n:
                res.append(cur)
                return
            dp(i + 1, cur[:])
            cur.append(nums[i])
            dp(i + 1, cur[:])
        dp(0,[])
        return res
            