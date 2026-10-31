class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        top = len(nums) - 1
        bottom = 0

        while bottom <= top:
            index = (bottom + top) // 2

            if nums[index] == target:
                return index
            elif nums[index] > target:
                top = index - 1
            else:
                bottom = index + 1

        return bottom