class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        numbers = []
        i = 0
        
        while i < len(str) and str[i] == ' ':
            i += 1
        
        if i < len(str) and str[i] == '+':
            sign = 1
            i += 1
        elif i < len(str) and str[i] == '-':
            sign = -1
            i += 1
            
        while i < len(str) and str[i].isnumeric():
            numbers.append(int(str[i]))
            i += 1
              
        total = 0
        #conversion
        for i in range(len(numbers)):
            index = len(numbers)-1-i
            total += numbers[index] * (10**i)

        total = sign * total
        if total > 2**31 -1:
            total = 2**31 -1
        if total < (-1)*2**31:
            total = (-1)*2**31
        return total
