class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd = []
        i,j = 0, len(nums) - 1

        while i<=j:
            if nums[i]%2 ==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
            if i!=j:
                if nums[j]%2 ==0:
                    even.append(nums[j])
                else:
                    odd.append(nums[j])
            i+=1
            j-=1
        return even + odd