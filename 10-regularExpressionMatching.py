class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
              
        if s and ((p[0] == s[0]) or (p[0] == '.')):
            match = True
        
        else: match = False
        
        if len(p) >=2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or match and self.isMatch(s[1:], p))
        else:
            return match and self.isMatch(s[1:], p[1:])
