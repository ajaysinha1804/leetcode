class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        a=0
        b=1
        for i in range(n):
            c=a
            a=a+b
            b=c
        return a


