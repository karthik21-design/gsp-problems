

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_cnt = 1, 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0]*len(nums)
        
        if zero_cnt != 0:
            return [0 if num != 0 else int(product) for num in nums] 
        else:
            return [int(product/num) for num in nums]