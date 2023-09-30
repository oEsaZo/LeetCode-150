class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start]<= nums[end]:
                return nums[start]
            mid = (start + end)//2
            if nums[start] > nums[mid]:
                end = mid
            else:
                start = mid+1
            
        