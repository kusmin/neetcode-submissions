class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viseted = {}
        for i, value in enumerate(nums):
            complemented = target - value 
            if complemented in viseted:
                return [viseted[complemented], i]
            viseted[value] = i
        