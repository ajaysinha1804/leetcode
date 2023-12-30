class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count=[0]*26
        for word in words:
            for c in word:
                count[ord(c)-ord('a')]+=1
        n=len(words)
        for val in count:
            if val%n !=0:
                return False
        return True
        
        