class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        index = 2
        one_step = 1
        two_step = 2
        while index < n:
            temp = one_step
            one_step = two_step
            two_step += temp
            index += 1
        return two_step   
        