class Solution(object):
    def NextGreatestElementOnRight(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        stack=[]
        top=-1
        ngeor=[]
        top=top+1
        stack.append(arr[-1])
        ngeor.append(-1)
        
        for i in range(len(arr)-2,-1,-1):
            #we have to pop the stack for an arr[i] until we either get arr[i]<stack[top] or stack is empty
            #if arr[i]<stack[top] , then append stack[top] into ngeor and push arr[i] into stack
            #if stack is empty, push arr[i] into stack and append -1 into ngeor
            
            while top!=-1 and arr[i]>stack[top]:
                del stack[top]
                top=top-1
            if top==-1:
                top=top+1
                stack.append(arr[i])
                ngeor.append(-1)
            elif arr[i]<stack[top]:
                ngeor.append(stack[top])
                top=top+1
                stack.append(arr[i])
                

        return ngeor[::-1] 
                
                    
#test-1    
arr1=[2,5,9,3,1,12,6,8,7]
sol=Solution()
l=sol.NextGreatestElementOnRight(arr1)
print(l)
