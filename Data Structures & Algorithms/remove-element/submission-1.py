class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

