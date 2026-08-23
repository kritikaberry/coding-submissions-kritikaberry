class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        k = 0
        for i in range(len(nums)):
        # If we find an element that is NOT the value we want to delete
            if nums[i] != val:
            # Copy it forward to our write tracking position
                nums[k] = nums[i]
            # Move our write pointer forward
                k += 1
        return k