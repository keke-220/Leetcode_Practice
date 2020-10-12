class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row = dict()
        for i in range(numRows):
            row[i] = []#store each row
        direction = 0 #increase index
        idx = 0
        if numRows == 1:
            return s
        for i in range(len(s)):
            print idx
            #print direction
            #print '\n'
            row[idx].append(s[i])
            if direction == 0:
                idx += 1
                #print idx
                if idx == numRows-1:
                    direction = 1
                    #idx -= 1
            elif direction == 1:
                idx -= 1
                if idx == 0:
                    direction = 0
        ret = []
        idx = 0
        for idx in range(0, numRows):
            print row[idx]
            for i in row[idx]:
                ret.append(i)
        return ''.join(ret)
