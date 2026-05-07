class Solution:
        def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
                self.ans=[]
                self.helper(nums,target,0,0,[])
                return self.ans

        def helper(self,nums,target,sum,idx,temp):
                if sum==target:
                        self.ans.append(temp[:])
                        return
                elif sum>target:
                        return
                if idx>=len(nums):
                        return
                temp.append(nums[idx])
                self.helper(nums,target,sum+nums[idx],idx,temp)
                temp.pop()
                self.helper(nums,target,sum,idx+1,temp)