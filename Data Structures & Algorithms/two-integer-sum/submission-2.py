class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index != index2:
                    encontrou = self.conferiSoma(nums[index], nums[index2], target)
                    if encontrou:
                        return [index, index2]


    def conferiSoma(self,primeiro, segundo, total):
        return primeiro + segundo == total    



        