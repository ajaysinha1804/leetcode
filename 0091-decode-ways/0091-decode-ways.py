class Solution:
    def numDecodings(self, s: str) -> int:
        curr = 0
        oneback=1
        twoback=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                curr = 0
            else:
                curr = oneback
                if i+1<len(s) and int(s[i]+s[i+1]) <= 26:
                    curr += twoback
            twoback = oneback
            oneback = curr
        return curr
        