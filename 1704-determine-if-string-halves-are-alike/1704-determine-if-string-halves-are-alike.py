class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=('a','e','i','o','u','A','E','I','O','U')
        mid=len(s)//2
        vowel1,vowel2=0,0
        for i in range(mid):
            char_a=s[i]
            char_b=s[mid + i]
            if char_a in vowels:
                vowel1 +=1
            if char_b in vowels:
                vowel2 +=1
        return vowel1 == vowel2
                
            
        