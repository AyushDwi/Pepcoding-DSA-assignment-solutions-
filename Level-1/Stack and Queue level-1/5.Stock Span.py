class Solution(object):
    def StockSpan(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        stack=[]
        top=-1
        span=[]
        for i in range(len(arr)):
            span.append(0)
        top=top+1
        stack.append(0)
        span[0]=1
        
        #stack will store the 'index' of the elements in arr
        #now if arr[i]>arr[stack[top]], then pop that element in the stack.
        #if stack becomes empty, then span of arr[i] is i+1,then we push i into the stack.
        #if arr[i]<arr[stack[top]], then span of arr[i] is number of pops before the condition +1,
        #then push i into the stack.
          
        for i in range(1,len(arr)):
            count=1
            while top!=-1 and arr[i]>arr[stack[top]]:
                del stack[top]
                top=top-1
                count=count+1
            if top==-1:
                span[i]=i+1
                stack.append(i)
                top=top+1
                
            elif arr[i]<=arr[stack[top]]:
                span[i]=count
                stack.append(i)
                top=top+1
                
        return span        
                                 
#test-1    
arr=[2,5,9,3,1,12,6,8,7]
sol=Solution()
l=sol.StockSpan(arr)
print(l)#[1,2,3,1,1,6,1,2,1]

#test-2   
arr=[1,1,3,4,5,6,1]
sol=Solution()
l=sol.StockSpan(arr)
print(l)#[1,1,3,4,5,6,1]
