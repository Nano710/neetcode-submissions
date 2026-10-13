class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x 
        res = 0
        while (left <= right):
            mid = left + (right - left)//2
            if (mid == 0 or mid <= x/mid ):
                res = mid
                left = mid +1
            else:
                right = mid -1

        return res
        
        