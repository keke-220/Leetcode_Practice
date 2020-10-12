import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ans = []
        for point in points:
            dist = 0
            for x in point:
                dist += x * x
        
            
            len_ans = len(ans)
            if len_ans < K:
                heapq.heappush(ans, [-1 * dist, point])
            elif -1 * dist > ans[0][0]:
                heapq.heapreplace(ans, [-1 * dist, point])
        ret = []
        for i in range(0, K):
            ret.append(heapq.heappop(ans)[1])
                
        return ret
