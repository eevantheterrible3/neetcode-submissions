class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_presum = []
        right_presum = []
        left_cum_sum = 1
        right_cum_sum = 1
        for e in nums:
            left_cum_sum *= e
            left_presum.append(left_cum_sum)
        
        for e in reversed(nums):
            right_cum_sum *= e
            right_presum.append(right_cum_sum)
        
        right_presum = list(reversed(right_presum))

        res = []
        for i in range(len(nums)):
            if((i - 1 >= 0) and (i + 1 <= (len(nums) - 1))):
                res.append(left_presum[i-1]*right_presum[i+1])
            elif(i - 1 < 0):
                res.append(right_presum[i+1])
            elif(i + 1 > len(nums) - 1):
                res.append(left_presum[i-1])
        
        return res