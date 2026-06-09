class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        n= len(nums)
        for i in range(n-2):
            a=nums[i]
            if a>0:
                break
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, n-1
            while l<r:
                s=a+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    res.add((a,nums[l],nums[r]))
                    l+=1
                    r-=1
        return [list(t) for t in res]
