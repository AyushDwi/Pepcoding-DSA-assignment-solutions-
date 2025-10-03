class Solution(object):
    def SelectionSort(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """Aim: place the largest element to its correct position."""

        for i in range(0,len(arr)-1):
            max_=arr[0]
            max_loc=0
            for j in range(0,len(arr)-i):
                if arr[j]>max_:
                    max_=arr[j]
                    max_loc=j
            arr[len(arr)-1-i],arr[max_loc]=arr[max_loc],arr[len(arr)-1-i]        
            print(arr)
        return arr            
        
#test-1      
arr=[10,6,12,18,3,1]
sol=Solution()
l=sol.SelectionSort(arr)
print(l)

