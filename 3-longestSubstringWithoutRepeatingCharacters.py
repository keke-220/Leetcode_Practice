class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        d = dict() #key: s[i] value: i
        d[l] = s[l]
        longest = 1
        while (r < len(s)):
            if (s[r] not in d.values()):
                d[r] = s[r]

                if (r-l+1>longest):
                    longest = r-l+1
            else:
                while (d[l] != s[r]):
                    d.pop(l)
                    l += 1
                d[r] = s[r]
                d.pop(l)
                l += 1
                
            
            r += 1
        return longest
