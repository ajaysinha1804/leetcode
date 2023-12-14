from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        onesRow=[0]*row
        onesCol=[0]*col
        for i in range(row):
            for j in range(col):
                onesRow[i] +=grid[i][j]
                onesCol[j] +=grid[i][j]
        diff=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                diff[i][j]=2*onesRow[i]+ 2*onesCol[j]-row-col 
        return diff
