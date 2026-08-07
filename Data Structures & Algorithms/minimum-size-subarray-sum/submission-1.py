class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        minLen = float("inf")

        for right in range(len(nums)):
            curr += nums[right]

            while(curr >= target):
                minLen = min(minLen, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if minLen == float("inf") else minLen
