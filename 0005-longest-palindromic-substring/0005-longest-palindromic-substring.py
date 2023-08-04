class Solution:
    def expand_around_center(self,left,right,s):
        while left >=0 and right < len(s) and s[left]==s[right]:
            left-=1
            right +=1 
        return s[left+1:right]
        
    def longestPalindrome(self, s: str) -> str:
        result=""
        for i in range(len(s)):
            pal1=self.expand_around_center(i,i,s)
            pal2=self.expand_around_center(i,i+1,s)
            if len(pal1)>len(pal2):
                longest_pal=pal1
            else:
                longest_pal=pal2
            result = longest_pal if len(longest_pal) > len(result) else result
        return result
            
        
                    
                    
                    
        