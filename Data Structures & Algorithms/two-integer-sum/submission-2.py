class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 0

        for left in range(len(nums)):
            complementary = target - nums[left]
            for right in range(left+1, len(nums)):
                if nums[right] == complementary:
                    return [left, right]
        