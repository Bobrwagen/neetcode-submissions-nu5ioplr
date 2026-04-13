class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dp(n,openB, closeB, cur):
            print(n,openB,closeB,cur)
            if n == 0:
                if openB == closeB:
                    return [cur]
                else: 
                    return None
            elif openB < closeB:
                return None
            else:
                left = dp(n-1, openB + 1, closeB, cur + '(')
                right = dp(n-1, openB, closeB + 1, cur + ')')
                print('Done for :', n)
                print(left)
                print(right)
                if left and right:
                    return left + right
                elif left: 
                    return left
                elif right is not None:
                    return right
                else: 
                    return None
        return dp(2*n,0,0,'')
        