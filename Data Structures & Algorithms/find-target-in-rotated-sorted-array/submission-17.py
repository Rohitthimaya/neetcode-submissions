class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while(i < j):
            middle = (i + j) // 2
            if(nums[middle] == target): return middle
            elif(nums[middle] > nums[j]): i = middle + 1
            else: j = middle
        
        minIdx = i
        print(nums[minIdx])

        if(minIdx == 0): l, r = 0, len(nums) - 1
        elif(nums[0] <= target <= nums[minIdx - 1]): l, r = 0, minIdx - 1
        else: l, r = minIdx, len(nums) - 1
        
        while(l <= r):
            mid = (l + r) // 2
            if(nums[mid] == target): return mid
            elif(nums[mid] < target): l = mid + 1
            else: r = mid - 1
        
        return -1


