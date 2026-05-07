class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        leastprice=float('inf')
        for i in prices:
            if i<leastprice:
                leastprice=i
            ans = max(ans,i-leastprice)
        return ans
        