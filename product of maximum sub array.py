class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        b=nums[::-1]
        for i in range(1,len(nums)):
            nums[i]*=nums[i-1] or 1
            b[i]*=b[i-1] or 1
        return max(nums+b)