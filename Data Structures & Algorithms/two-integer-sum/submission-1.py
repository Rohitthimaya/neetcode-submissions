class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            numToFind = target - num
            if numToFind in hashMap:
                return [hashMap[numToFind], i]
            hashMap[num] = i
        return [-1, -1]