class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=float('-inf')
        max2=float('-inf')
        for i in range(len(nums)):
            if nums[i]>max1:
                max2=max1
                max1=nums[i]
            elif nums[i]>max2:
                max2=nums[i]
            
        return (max1-1)*(max2-1)
        
        