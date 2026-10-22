class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        not_val_count = 0

        for index in range(len(nums)):
            if nums[index] != val:
                nums[not_val_count] = nums[index]
                not_val_count += 1
        
        return not_val_count
