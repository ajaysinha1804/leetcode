class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        negative=False
        if x<0:
            x=-x
            negative=True
        while x>0:
            rem=x%10
            ans=ans*10 + rem
            x=x//10
        if ans > 2**31 -1 or ans < -2**31:
            return 0
        if negative:
            ans=-ans
        return ans
            