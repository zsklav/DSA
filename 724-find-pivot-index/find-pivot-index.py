class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftsum=0
        totalsum=sum(nums)
        for i in range(len(nums)):
            if leftsum==totalsum-nums[i]-leftsum:
                return i
            else:
                leftsum+=nums[i]
        return -1