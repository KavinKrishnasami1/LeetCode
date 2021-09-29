class Solution:
    def reverse(self, x: int) -> int:
        s = 0
        if x > 0:
            s = int(str(x)[::-1])
        else:
            s = -1 * int(str(x*-1)[::-1])
        
        if s not in range(-2**31, 2**31 - 1):
            return 0
        
        return s