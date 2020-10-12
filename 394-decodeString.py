class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ###stack
        stack = []
        res = []
        for i in range(0, len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                decoded = []
                while stack[-1] != '[':
                    decoded.append(stack.pop())
                stack.pop()
                indexs = []
                while stack and stack[-1].isnumeric():
                    indexs.append(stack.pop())
                index = int(''.join(indexs[::-1])) -1 
                length = len(decoded)
                for j in range(0, index): 
                    for k in range(0, length):
                        decoded.append(decoded[k])
                #print (decoded)
                for ele in decoded[::-1]:
                    stack.append(ele)           
        s = ''.join(stack)
        return s
