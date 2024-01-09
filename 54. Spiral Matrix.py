class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L=[]
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            for j in range(n):
                L.append(matrix[0][j])
            return L
        if n == 1:
            for i in range(m):
                L.append(matrix[i][0])
            return L
        r = 1

        while m- 2*r >= 0 and n-2*r >=-1:
            for j in range(-1+r,n-r):
                L.append(matrix[r-1][j])
            #print(L)
            for i in range(r-1,m-r):
                L.append(matrix[i][n-r])
           # print(L)
            if m == 2*r-1:
                return L
            for j in range(n-r,r-1,-1):
                i = m-r
                L.append(matrix[i][j])
            #print(L)
            if n == 2*r -1:
                L.append(matrix[m-r][n-r])
                return L
            for i in range(m-r,r-1,-1):
                j = r-1
                L.append(matrix[i][j])
            #print(L)
            r += 1
            #print(r)
        if m - 2*r == -1 and n-2*r >= -1:
            for j in range (r-1,n-r+1):
                L.append(matrix[r-1][j])

        return L


            