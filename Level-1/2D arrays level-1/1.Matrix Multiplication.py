class Solution(object):
    def MatrixMultiplication(self, Matrix_1,Matrix_2):
        """
        :type Matrix_1: List[List[int]]
        :type Matrix_2: List[List[int]]
        :rtype: List[List[int]]
        """
        r1=len(Matrix_1)
        c1=len(Matrix_1[0])
        r2=len(Matrix_2)
        c2=len(Matrix_2[0])

        if c1!=r2:
            return -1
        
        matrix=[]
        for i in range(r1):
                matrix.append([0]*c2)

        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    matrix[i][j]+=Matrix_1[i][k]*Matrix_2[k][j]
        return matrix
#test-1    
M1=[[12,7,3],[4,5,6],[7,8,9]]
M2=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]
sol=Solution()
l=sol.MatrixMultiplication(M1,M2)
print(l)
    
