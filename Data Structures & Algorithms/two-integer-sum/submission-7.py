class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            newArray = nums[index + 1:]
            for index2, value2 in enumerate(newArray):
                encontrou = self.conferiSoma(nums[index], nums[index2 + index + 1], target)
                if encontrou:
                    return [index, index2 + index + 1]
                    


    def conferiSoma(self,primeiro, segundo, total):
        return primeiro + segundo == total 