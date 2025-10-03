class Solution(object):
    def SelectionSort(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """Aim: place the smallest element to its correct position."""

        for i in range(0,len(arr)-1):
            min_=arr[i]
            min_loc=i
            for j in range(i+1,len(arr)):
                if arr[j]<min_:
                    min_=arr[j]
                    min_loc=j
            arr[i],arr[min_loc]=arr[min_loc],arr[i]        
            print(arr)
        return arr            
        
#test-1      
arr=[10,6,12,18,3,1]
sol=Solution()
l=sol.SelectionSort(arr)
print(l)

