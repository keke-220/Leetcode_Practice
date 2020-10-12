class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        pre = strs[0]
        for s in strs:
            if pre == "": return pre
            if (len(pre) > len(s)):
                pre = pre[:len(s)]
            for i in range(min(len(s), len(pre))):
            
                if s[i] != pre[i]:
                    pre = pre[:i]
                    break
            print pre
        return pre
