class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        st = []

        for i in s:
            if i == '{' or i == '[' or i == '(':
                st.append(i)
            elif st and st[len(st)-1] == mp[i]:
                print(mp[i])
                st.pop()
            else:
                return False
        return not st



            
    