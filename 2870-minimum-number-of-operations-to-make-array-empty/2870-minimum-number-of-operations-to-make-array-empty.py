class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations=0
        counter=Counter(nums)
        for i in counter.values():
            if i==1:
                return -1
            elif i%3==0:
                operations +=i//3 
            else:
                operations +=(i//3)+1
        return operations
        