class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        k = 1

        while i<j and j<len(nums):
            if nums[i] != nums[j]:
                nums[k] = nums[j]
                k+=1
            i+=1
            j+=1

        return k
                


        