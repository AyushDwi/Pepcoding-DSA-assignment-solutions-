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
        minr=0
        minc=0
        maxr=r1-1
        maxc=c1-1
        while(count<r1*c1):
          while(i<=maxr and j==minc):
              lst.append(Matrix[i][j])
              count+=1
              i=i+1
              if i==maxr+1:
                  i=maxr
                  j=minc+1
          while(j<=maxc and i==maxr):
              lst.append(Matrix[i][j])
              count+=1
              j=j+1
              if j==maxc+1:
                  j=maxc
                  i=maxr-1
          while(i>=minr and j==maxc):
              lst.append(Matrix[i][j])
              count+=1
              i=i-1
              if i==minr-1:
                  i=minr
                  j=maxc-1
          while(j>=minc+1 and i==minr):
              lst.append(Matrix[i][j])
              count+=1
              j=j-1
              if j==minc:
                  minc=minc+1
                  minr=minr+1
                  maxc=maxc-1
                  maxr=maxr-1
                  i=minr
                  j=minc

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

#test-3
M3=[[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45],[51,52,53,54,55]]
l=sol.waveTraversal(M3)
print(l)
