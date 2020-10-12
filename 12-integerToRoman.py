class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = []
        numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        #symDict = dict()
        for j in range(len(numbers)):
            t = num/numbers[j]
            num = num%numbers[j]
            for i in range(t):
                s.append(symbols[j])
        return ''.join(s)
