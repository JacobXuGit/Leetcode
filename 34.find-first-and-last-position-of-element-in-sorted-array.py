#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        def findBounds(l, r, isFirst):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    if isFirst:
                        if mid == left or nums[mid-1] < target:
                            return mid
                        else:
                            r = mid - 1
                    else:
                        if mid == right or nums[mid+1] > target:
                            return mid
                        else:
                            l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        lb = findBounds(left, right, True)
        rb = findBounds(left, right, False)
        if lb == None and rb == None:
            return [-1, -1]
        return [lb, rb]                                        

# @lc code=end

