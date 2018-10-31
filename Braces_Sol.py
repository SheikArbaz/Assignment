class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        st=[]
        for ch in A: 
            if (ch == ')'): 
                top = st.pop(-1)
                flag = True
    
                while (top != '('):
      
                    if (top == '+' or top == '-' or  
                        top == '*' or top == '/'): 
                        flag = False; 
      
                    top = st.pop(-1)
      
                if (flag):
                    return 1; 
      
            else:
                st.append(ch)
        return 0
