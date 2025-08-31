class Solution(object):
    def NextGreatestElementOnRight(self,arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        stack=[]
        top=-1
        ngeor=[]
        for i in arr:
            ngeor.append(-1)
        top=top+1
        stack.append(arr[0])

        for i in range(1,len(arr)):
            #if arr[i] is greater than stack[top],pop the elements from the stack coressponding to
            #those elements in stack, write ngeor for those elements as arr[i]
            #if arr[i]<stack[top], push arr[i] into stack, and do not update corresponding ngeor
            #if stack is empty, then push arr[i] into stack, and do not update corresponding ngeor

            while top!=-1 and arr[i]>stack[top]:
                temp=stack[top]
                del stack[top]
                top=top-1
                ngeor[arr.index(temp)]=arr[i]
                
                
            if top==-1:
                top=top+1
                stack.append(arr[i])
                
            elif arr[i]<stack[top]:
                
                top=top+1
                stack.append(arr[i])
                

        return ngeor
                
                    
#test-1    
arr1=[2,5,9,3,1,12,6,8,7]
sol=Solution()
l=sol.NextGreatestElementOnRight(arr1)
print(l)
