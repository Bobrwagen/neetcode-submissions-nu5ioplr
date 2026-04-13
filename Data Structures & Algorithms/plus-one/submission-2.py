class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = True
        digit = len(digits) -1
        while add and digit >= 0:
            digits[digit] = (digits[digit] + 1) % 10
            add = digits[digit] == 0
            digit -= 1
        if digit < 0 and digits[digit+1] == 0:
            digits.insert(0,1)
        return digits
        
        