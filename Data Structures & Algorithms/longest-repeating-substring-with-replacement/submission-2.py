class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp={}
        i=0
        maxfreq=0
        ans=0
        for idx,j in enumerate(s):
            mp[j]=mp.get(j,0)+1
            maxfreq = max(maxfreq,mp[j])
            while idx-i+1-maxfreq>k:
                mp[s[i]]-=1
                i+=1
            ans = max(ans,idx-i+1)

        return ans

            
