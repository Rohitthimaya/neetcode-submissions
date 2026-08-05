class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMost = []
        rightMost = []
        res = []

        # [1, 1, 2, 8]
        runningProduct = 1
        for num in nums:
            leftMost.append(runningProduct)
            runningProduct *= num
        print(leftMost)

        runningProduct = 1
        for num in reversed(nums):
            rightMost.append(runningProduct)
            runningProduct *= num
        rightMost = list(reversed(rightMost))
        
        for i in range(len(nums)):
            res.append(leftMost[i] * rightMost[i])
        
        return res
        
