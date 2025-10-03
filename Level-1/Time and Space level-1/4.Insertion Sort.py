class Solution(object):
    def InsertionSort(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        """Aim: to sort small chunks of array."""

        for i in range(1,len(arr)):
            for j in range(i-1,-1,-1):
                if arr[j+1]<arr[j]:
                    arr[j+1],arr[j]=arr[j],arr[j+1]
                    print(arr)
        return arr

                 
        
#test-1      
arr=[10,6,12,18,3,1]
sol=Solution()
l=sol.InsertionSort(arr)
print(l)

