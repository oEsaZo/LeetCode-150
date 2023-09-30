class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        if len(res) == 1:
            res.append(res[0])        
        return [min(res), max(res)]

            
