class Solution(object):
    def LargestAreaHistogram(self,arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #my initial thoughts: we need to find out the number of consecutive histogram bars
        #that are >= a given height.

        #for an element, next smallest element on the left is the left boundary, and
        #next smallest element on the right is the right boundary of the rectangle.

        #we will store the index of the right boundary and left boundary element corresponding
        #to arr[i] in rb[i] and lb[i] espectively. 

        rb=[]
        rb_stack=[]
        rb_top=-1
        rb_stack.append(len(arr)-1)
        rb_top+=1
        
        lb=[]
        lb_stack=[]
        lb_top=-1
        lb_stack.append(0)
        lb_top+=1
        
        for i in range(len(arr)):
            rb.append(0)
            lb.append(0)

        rb[-1]=len(arr)
        for i in range(len(arr)-2,-1,-1):
            while rb_top!=-1 and arr[i]<arr[rb_stack[rb_top]]:
                del rb_stack[rb_top]
                rb_top=rb_top-1
            if rb_top==-1:
                rb[i]=len(arr)
            else:
                rb[i]=rb_stack[rb_top]
            rb_stack.append(i)
            rb_top+=1

        lb[0]=-1
        for i in range(1,len(arr)):
            while lb_top!=-1 and arr[i]<arr[lb_stack[lb_top]]:
                del lb_stack[lb_top]
                lb_top=lb_top-1
            if lb_top==-1:
                lb[i]=-1
            else:
                lb[i]=lb_stack[lb_top]
            lb_stack.append(i)
            lb_top+=1

        MaxArea=0    
          
        for i in range(0,len(arr)):
            width=rb[i]-lb[i]-1
            area=arr[i]*width
            if area>MaxArea:
                MaxArea=area
        return MaxArea  
                                 
#test-1    
arr=[2,5,9,3,1,12,6,8,7]
sol=Solution()
l=sol.LargestAreaHistogram(arr)
print(l)

#test-2   
arr=[1,1,3,4,5,6,1]
sol=Solution()
l=sol.LargestAreaHistogram(arr)
print(l)

#test-3 
arr=[6,2,5,4,5,1,6]
sol=Solution()
l=sol.LargestAreaHistogram(arr)
print(l)
