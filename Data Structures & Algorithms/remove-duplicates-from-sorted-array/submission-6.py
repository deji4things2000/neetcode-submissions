class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)-1
        i,j = 0, 1

        while j<=n:
            if nums[i] != nums[j]:
                nums[k] = nums[j]
                k+=1
            i+=1
            j+=1
        return k
        