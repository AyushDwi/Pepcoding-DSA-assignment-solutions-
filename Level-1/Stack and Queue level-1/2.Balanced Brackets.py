class Solution(object):
    def DuplicateBrackets(self,s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        top=-1
        
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                top=top+1
                stack.append(s[i])
                print(stack)

            elif s[i]==')':
                if len(stack)==0 or stack[top]=='[' or stack[top]=='{':
                   return False
                elif stack[top]=='(':
                   del stack[top]
                   top=top-1
                   print(stack)

            elif s[i]==']':
                if len(stack)==0 or stack[top]=='(' or stack[top]=='{':
                   return False
                elif stack[top]=='[':
                   del stack[top]
                   top=top-1
                   print(stack)
                   
            elif s[i]=='}':
                if len(stack)==0 or stack[top]=='[' or stack[top]=='(':
                   return False
                elif stack[top]=='{':
                   del stack[top]
                   top=top-1
                   print(stack)
        if len(stack)==0:
            return True
        else:
            return False
                    
#test-1    
s1="[(a+b)+{(c+d)*(e/f)}]"
sol=Solution()
l=sol.DuplicateBrackets(s1)
print(l)

#test-2    
s2="[(a+b)+{(c+d)*(e/f)]}"
l=sol.DuplicateBrackets(s2)
print(l)

#test-3   
s3="[(a+b)+{(c+d)*(e/f)}"
l=sol.DuplicateBrackets(s3)
print(l)   

#test-4
s4="([(a+b)+{(c+d)*(e/f)}]"
l=sol.DuplicateBrackets(s4)
print(l)

#test-5
s5="[(a+b)+{(c+d)*(e/f)}])"
l=sol.DuplicateBrackets(s5)
print(l) 
