class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        m = len(matrix)
        n = len(matrix[0])
        t =0
        b = m-1
        l = 0
        r = n-1
        while t <= b and l <= r:
            #right
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t +=1
            #down
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            #left
            if t <= b:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b-=1
            #up
            if l <= r:                    
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res
        