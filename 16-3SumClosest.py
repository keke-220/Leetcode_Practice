class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1
            while (lo < hi):
                s = nums[lo] + nums[hi] + nums[i]
                if abs(target - s) < abs(diff):
                    diff = target-s
                if s<target:
                    lo+=1
                else: hi -= 1
                if diff == 0:
                    break
        return target-diff
