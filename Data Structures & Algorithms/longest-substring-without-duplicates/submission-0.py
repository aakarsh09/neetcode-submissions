class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        i=0
        ans=0
        for idx,j in enumerate(s):
            while j in mp:
                mp.pop(s[i])
                i+=1
            mp[j]=idx
            ans=max(ans,idx-i+1)
        return ans
