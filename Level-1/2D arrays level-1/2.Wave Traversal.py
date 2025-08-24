class Solution(object):
    def waveTraversal(self, Matrix):
        """
        :type Matrix: List[List[int]]
        :rtype: List[[int]]
        """
        r1=len(Matrix)
        c1=len(Matrix[0])
        lst=[]
        i=0
        j=0
        count=0
        while(count<r1*c1):
          while(i<=r1-1 and j%2==0 and j<=c1-1):
              lst.append(Matrix[i][j])
              count+=1
              i=i+1
              if i==r1:
                j+=1
                i=r1-1
                
          while(i>=0 and j%2==1 and j<=c1-1):
              lst.append(Matrix[i][j])
              count+=1
              i=i-1
              if i==-1:
                j+=1
                i=0
        return lst
#test-1    
M1=[[12,7,3],[4,5,6],[7,8,9]]
sol=Solution()
l=sol.waveTraversal(M1)
print(l)

#test-2
M2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
l=sol.waveTraversal(M2)
print(l)    
