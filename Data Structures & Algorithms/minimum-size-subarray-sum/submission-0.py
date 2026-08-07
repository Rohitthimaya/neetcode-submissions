class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        maxCount = 10000
        for i in range(len(nums)):
            j = i + 1
            curr = nums[i]
            while(j < len(nums) and curr < target):
                curr += nums[j]
                j += 1
            if(curr >= target):
                maxCount = min(maxCount, j - i)
            if(maxCount == 10000): return 0
        return maxCount
