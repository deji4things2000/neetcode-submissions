class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def rotate_mini(nums, i, j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            return nums

        rotate_mini(nums, 0, n-1)
        rotate_mini(nums, 0, k-1)
        rotate_mini(nums, k, n-1)
        