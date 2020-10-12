class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #dynamic programming
        
        if s == '':
            return ''
        rows, cols = (len(s), len(s)) 
        m = [[0 for i in range(cols)] for j in range(rows)]
        #print(m)
        for i in range(len(s)):
            m[i][i] = 1
        #print(m)

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                m[i][i+1] = 1
            else:
                m[i][i+1] = 0

        for t in range(2, len(s)+1):
             for i in range(len(s)-2):
                
                j = i+t
                #print (i)
                #print (j)
                if j <= len(s)-1:
                    if m[i+1][j-1] == 1 and s[i] == s[j]:
                        m[i][j] = 1
                    else: m[i][j] = 0
        #print(m)
        longest = 1
        l = 0
        r = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j-i+1 >= longest and m[i][j] == 1:
                    l = i
                    r = j
                    longest = j-i+1
        ret = []
        for x in range(l, r+1):
            ret.append(s[x])
        return ''.join(ret)
