class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0
        for num in numsSet:
            if(num - 1) in numsSet:
                pass
            else:
                count = 1
                tmp = num
                while((tmp + 1) in numsSet):
                    count += 1
                    tmp += 1
                maxCount = max(maxCount, count)
        return maxCount