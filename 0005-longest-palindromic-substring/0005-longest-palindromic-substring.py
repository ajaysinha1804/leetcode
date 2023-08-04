class Solution:
    def is_palindromic(self,substring):
        return substring==substring[::-1]
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max_length=0
        res=""
        for i in range(n):
            for j in range(i,n):
                substring=s[i:j+1]
                if self.is_palindromic(substring) and len(substring)>max_length:
                    max_length=len(substring)
                    res=substring 
        return res
                    
                    
                    
        