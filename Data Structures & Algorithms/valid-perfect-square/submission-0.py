class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        left = 0
        right = x 
        res = 0
        while (left <= right):
            mid = left + (right - left)//2
            if (mid == 0 or mid == x/mid ):
                return True
            elif (mid > x/mid ):
                right = mid -1
            else:
                left = mid +1

        return False