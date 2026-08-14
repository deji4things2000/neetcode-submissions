class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1
        k=1

        while j<n:
            if nums[i] != nums[j]:
                nums[k] = nums[j]
                k+=1
            i+=1
            j+=1
        return k

        