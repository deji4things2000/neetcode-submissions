class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1, n-1

                while left<right:
                    sm = nums[i] + nums[j] + nums[left] + nums[right]

                    if sm == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left] ==  nums[left+1]:
                            left+=1
                        while left<right and nums[left] ==  nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif sm<target:
                        left+=1
                    else:
                        right-=1
        return res
                        
                

            