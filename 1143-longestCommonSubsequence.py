class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        array = [[0 for i in range(0, len(text1)+1)] for j in range(0, len(text2)+1)]
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                if text1[j-1] == text2[i-1]:
                    array[i][j] = array[i-1][j-1] + 1
                else:
                    array[i][j] = max(array[i-1][j], array[i][j-1])
        return array[len(text2)][len(text1)]
