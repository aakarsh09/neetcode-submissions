class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        ans=[]
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            j=len(nums)-1
            mid=i+1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while mid<j:
                if nums[i]+nums[j]+nums[mid]==0:
                    ans.append([nums[i],nums[j],nums[mid]])
                    mid+=1
                    j-=1
                    while mid<j and nums[mid]==nums[mid-1]: 
                        mid+=1
                elif nums[i]+nums[j]+nums[mid]<0:
                    mid+=1
                else:
                    j-=1
        return ans

