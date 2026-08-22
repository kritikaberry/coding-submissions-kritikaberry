class Solution:
    def twoSum(self, nums: List[int], target: int): #-> List[int]:
        if(len(nums)==0):
            return []
        ans = {}
        for i in range(len(nums)):
            print(i)
            diff = target - nums[i] 
            if diff in ans: 
                return([ans[diff],i])
            ans[nums[i]]= i 