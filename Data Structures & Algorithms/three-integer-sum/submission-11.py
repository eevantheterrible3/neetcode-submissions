class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        tuples = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
        
            j = i + 1
            k = len(nums) - 1

            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    if tuple([nums[i], nums[j], nums[k]]) not in tuples:
                        res.append([nums[i], nums[j], nums[k]])
                        tuples.append(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
        
        return res
                





        
        

        