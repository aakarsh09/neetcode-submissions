from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in strs:
            sorted_val = "".join(sorted(i))
            mp[sorted_val].append(i)
        return list(mp.values())        