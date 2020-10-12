class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #continuly moving the longer line, inital line position will be leftmost and rightmost
        l = 0
        r = len(height)-1
        sumh = 0
        while (r > l):
            sumh  = max(sumh, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l+=1
            else: r-=1
        return sumh
