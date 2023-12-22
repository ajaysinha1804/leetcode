class Solution:
    def maxScore(self, s: str) -> int:
        ans=0
        for i in range(len(s)-1):
            curr=0
            left_curr=0
            right_curr=0
            res=0
            for j in range(i+1):
                if s[j]=="0":
                    left_curr +=1
            for j in range(i+1,len(s)):
                if s[j]=="1":
                    right_curr +=1
            res=left_curr + right_curr
            ans =max(ans,res)
        return ans
                