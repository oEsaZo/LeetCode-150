class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # peak = 0
            
        # for i in range(1,len(nums)-2):
        #     peak = max(nums[i-1], nums[i+1], nums[i])
        #     if peak in nums:
        #         return nums.index(peak)
        return nums.index(max(nums)) 