class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=('a','e','i','o','u','A','E','I','O','U')
        left,right=0,len(s)-1
        vowel_count =0
        while left < right:
            if s[left] in vowels:
                vowel_count +=1
            if s[right] in vowels:
                vowel_count -=1
            left +=1
            right -=1
        return vowel_count ==0
                
            
        