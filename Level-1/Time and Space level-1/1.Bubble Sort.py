class Solution(object):
    def BubbleSort(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        for i in range(0,len(arr)-1):
            
            for j in range(1,len(arr)-i):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    print(arr)
        return arr            
        
#test-1      
arr=[10,6,12,18,3,1]
sol=Solution()
l=sol.BubbleSort(arr)
print(l)

