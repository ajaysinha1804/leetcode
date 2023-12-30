class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count=defaultdict(int)
        for word in words:
            for c in word:
                count[c]+=1
        n=len(words)
        for val in count.values():
            if val%n !=0:
                return False
        return True
        
        