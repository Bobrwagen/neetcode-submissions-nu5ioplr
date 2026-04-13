class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:]
        suffix = nums[:]
        p_curr = 1
        s_curr = 1
        for i in range(len(nums)):
            print(i)
            p_temp = prefix[i]
            s_temp = suffix[-i-1]
            prefix[i] = p_curr
            suffix[-i-1] = s_curr
            p_curr *= p_temp
            s_curr *= s_temp
        res = []
        for p,s in zip(prefix,suffix):
            res.append(p*s)
        return res


        