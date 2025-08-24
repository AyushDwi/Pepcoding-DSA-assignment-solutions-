class Solution(object):
    def DuplicateBrackets(self,s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        top=-1
        
        for i in range(len(s)):
            if s[i]!=')':
                top=top+1
                stack.append(s[i])
                print(stack)
            elif s[i]==')':
                if stack[top]=='(':
                    return True
                else:
                    while stack[top]!='(':
                        del stack[top]
                        top=top-1
                        print(stack)
                    del stack[top]
                    top=top-1
                    print(stack)
        return False             
                    
#test-1    
s1="((a+b)+(c+d))"
sol=Solution()
l=sol.DuplicateBrackets(s1)
print(l)

#test-2    
s2="(a+b)+((c+d))"
l=sol.DuplicateBrackets(s2)
print(l)    
