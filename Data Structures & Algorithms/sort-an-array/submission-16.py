class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(num, left, right):
            if left >= right:
                return

            mid = (left+right)//2
            num[left], num[mid] = num[mid], num[left]

            l = left
            r = left + 1

            while r <= right:
                if num[r] < num[left]:
                    l+=1
                    num[r], num[l] = num[l], num[r]
                r+=1
            num[l], num[left] = num[left], num[l]
            quick(num, left, l-1)
            quick(num, l+1, right)
        quick(nums, 0, len(nums)-1)
        return nums
            