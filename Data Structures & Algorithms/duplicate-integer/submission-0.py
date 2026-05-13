class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set(map(lambda x: x, nums))
        print(elems)
        return len(elems) != len(nums)
