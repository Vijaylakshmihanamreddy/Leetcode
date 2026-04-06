class Solution(object):
    def searchRange(self, nums, target):
        def findBound(isFirst):
            low, high = 0, len(nums) - 1
            bound = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        high = mid - 1  # Look left for first position
                    else:
                        low = mid + 1   # Look right for last position
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound
        
        return [findBound(True), findBound(False)]

        