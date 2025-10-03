class Solution(object):
    def QuickSort(self,arr,start,end):
        """
        :type arr: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        if start<end:
            pIndex=self.Partition(arr,start,end)
            self.QuickSort(arr,start,pIndex-1)
            self.QuickSort(arr,pIndex+1,end)
        
        
    def Partition(self,arr,start,end):
        """
        :type arr: List[int]
        :type start: int
        :type end: int
        :rtype: int
        """
        pivot=arr[end]
        pIndex=start
        for i in range(start,end):
            if arr[i]<=pivot:
                arr[i],arr[pIndex]=arr[pIndex],arr[i]
                pIndex+=1
        arr[pIndex],arr[end]=arr[end],arr[pIndex]
        return pIndex
                 
        
#test-1      
arr=[10,6,12,18,3,11]
sol=Solution()
sol.QuickSort(arr,0,len(arr)-1)
print(arr)

#test-2    
arr=[7,2,1,6,8,5,3,4]
sol=Solution()
sol.QuickSort(arr,0,len(arr)-1)
print(arr)
