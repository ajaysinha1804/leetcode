class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        elif n==0:
            return True
        elif n%10==0:
            return False
        dummy=n
        rev_no=0
        while n>0:
            last_digit = n%10
            rev_no=(rev_no)*10 + last_digit
            n=n//10
        if rev_no==dummy:
            return True
        else:
            return False