class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #binary search
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, min(m, n)):
            v_found = self.binary_search(matrix, target, i, True)
            h_found = self.binary_search(matrix, target, i, False)
            if v_found or h_found:
                return True
        return False
    
    def binary_search(self, matrix, target, start, isV):
        lo = start
        if isV:
            hi = len(matrix[0]) - 1
        else:
            hi = len(matrix) - 1
        while (lo <= hi):
            mid = (lo + hi) // 2
            print lo
            print hi
            print mid
            if isV:
                if matrix[start][mid] > target:
                    hi = mid - 1
                elif matrix[start][mid] < target:
                    lo = mid + 1
                else: 
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        return False
