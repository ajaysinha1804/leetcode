class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=0
        curr_index=nums[0]
        for i in range(1,len(nums)):
            res=max(res,(curr_index -1)*(nums[i]-1))
            curr_index=max(curr_index,nums[i])
        return res
        
        