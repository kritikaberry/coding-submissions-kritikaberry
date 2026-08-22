class Solution:
    def isValid(self, s: str) -> bool:
        if(s==''):
            return True
        st = []
        for i in s:
            if i == '(':
                st.append(')')
            elif i == '[':
                st.append(']')
            elif i == '{':
                st.append('}')
            elif not st or st.pop() != i:
                return False
        
        if len(st) == 0:
            return True
        else:
            return False


                
        
