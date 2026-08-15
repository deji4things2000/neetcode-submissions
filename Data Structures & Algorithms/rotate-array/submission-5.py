class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        def rotate(num, left, right):
            while left<=right:
                num[left], num[right] = num[right], num[left]
                left+=1
                right-=1
            return num

        rotate(nums, 0, n-1)
        rotate(nums, 0, k-1)
        rotate(nums, k, n-1) 

        