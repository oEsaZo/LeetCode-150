class Solution:
    def isHappy(self, n: int) -> bool:
        h = set()
        while n != 1:
            if n in h: 
                return False
            h.add(n)
            n = sum([int(i)**2 for i in str(n)])
        else:
            return True
        