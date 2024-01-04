class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations=0
        counter=Counter(nums)
        for i in counter.values():
            if i==1:
                return -1
            operations +=ceil(i/3)
        return operations
        