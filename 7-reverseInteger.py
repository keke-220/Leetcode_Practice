class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 2**31-1 or x< -2**31:
            return 0
        else:
            if x>0:
                ret = []
            elif x < 0:
                ret = ['-']
                x = -x
            else:
                return 0
            count = len(str(x))
            for i in range(count):
                num = x%10
                x = (x-num)/10
                ret.append(str(num))
            p = 0
            for i in range(len(ret)):
                if ret[0] == '-':
                    p = 1
                if ret[p] == '0':
                        ret.pop(p)
                else:
                    break
            ret = ''.join(ret)
            print ret
            if int(ret) > 2**31-1 or int(ret)< -2**31:
                return 0
            return ret
