class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit = []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else: letter.append(log.split())
                
        letter.sort(key = lambda x: x[0])
        letter.sort(key = lambda x: x[1:])
        print letter
        ans = []
        for log in letter:
                        
            s = ' '
            ans.append(s.join(log))
        for log in digit:
            ans.append(log)
        return ans
                
