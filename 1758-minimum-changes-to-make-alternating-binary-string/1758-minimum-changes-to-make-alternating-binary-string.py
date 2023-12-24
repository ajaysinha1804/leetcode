class Solution:
    def minOperations(self, s: str) -> int:
        n=sum(a==b for a,b in zip(s,cycle("01")))
        return min(n,len(s)-n)
            
                
                
        