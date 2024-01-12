class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=('a','e','i','o','u','A','E','I','O','U')
        mid=len(s)//2
        vowel_count=0
        for i in range(mid):
            char_a=s[i]
            char_b=s[mid + i]
            if char_a in vowels:
                vowel_count +=1
            if char_b in vowels:
                vowel_count -=1
        return vowel_count ==0
                
            
        