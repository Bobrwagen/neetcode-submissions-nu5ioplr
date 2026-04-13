class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            l = numbers[left]
            r = numbers[right]
            s = l + r
            if s == target:
                return [left + 1,right +1]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []
        