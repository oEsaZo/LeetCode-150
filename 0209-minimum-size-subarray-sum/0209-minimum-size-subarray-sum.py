class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i,j = 0,0
        total = nums[0]
        min_len = float("inf")
        while j<= len(nums)-1:
            if total < target:
                j+=1
                if j <= len(nums) -1:
                    total += nums[j]
            elif total >= target:
                min_len = min(min_len, j-i+1)
                total-= nums[i]
                i+=1
        return min_len if min_len != float("inf") else 0       



        