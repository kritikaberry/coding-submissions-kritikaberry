class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False
        l = len(nums)
        checker = set()
        for num in nums:
            checker.add(num)
        if(l != len(checker)):
            return True
        return False
