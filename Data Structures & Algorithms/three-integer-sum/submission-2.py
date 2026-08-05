class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i, num in enumerate(nums):
            target = -num
            hashMap = {}
            for j in range(i + 1, len(nums)):
                numToFind = target - nums[j]
                if(numToFind in hashMap):
                    triplet = tuple(sorted([num, nums[j], numToFind]))
                    res.add(triplet)
                else:
                    hashMap[nums[j]] = j
        return [list(t) for t in res]
