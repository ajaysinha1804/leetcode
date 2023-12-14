class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=len(mat)
        col=len(mat[0])
        r=[0]*row
        c=[0]*col
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1:
                    r[i]+=1
                    c[j]+=1
        count=0
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1 and r[i]==1 and c[j]==1:
                    count +=1
        return count