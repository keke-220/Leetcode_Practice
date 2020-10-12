class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {}
        pair[')'] = '('
        pair[']'] = '['
        pair['}'] = '{'
        for i in range(len(s)):
            if stack!=[]:
                
                if s[i] in pair:
                    top = stack.pop()
                    if top != pair[s[i]]:
                        stack.append(top)
                        stack.append(s[i])
                    
                else: stack.append(s[i])
                
            else:stack.append(s[i])
        if stack ==[]:
            return True
        else: return False
