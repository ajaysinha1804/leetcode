class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        case=len(arr)//4
        p=arr[0]
        count=1
        for i in range(1,len(arr)):
            if arr[i]==p:
                count +=1
            else:
                count = 1
            if count > case:
                return arr[i]
            else:
                p=arr[i]
        return p
        