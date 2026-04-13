class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0,temperatures[0])]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            _,t = stack[-1]
            if temp > t:
                while stack and t < temp:
                    ind,_ = stack.pop()
                    res[ind] = i - ind
                    if stack:
                        _,t = stack[-1]
            stack.append((i,temp))
            print(res, stack)
        return res

        