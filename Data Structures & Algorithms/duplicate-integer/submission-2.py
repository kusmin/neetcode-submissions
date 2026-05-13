class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set(map(lambda x: x, nums))
        return len(elems) != len(nums)
