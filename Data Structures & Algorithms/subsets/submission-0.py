class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.helper(nums,0,[])
        return self.ans

    def helper(self,nums,idx,temp):
        if idx>=len(nums):
            self.ans.append(temp[:])
            return
            
        temp.append(nums[idx])
        self.helper(nums,idx+1,temp)
        temp.pop()
        self.helper(nums,idx+1,temp)
    