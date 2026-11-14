class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def qs(num, left, right):
            if left>=right:
                return
            
            mid = (left+right)//2

            num[mid], num[left] = num[left], num[mid]

            l = left
            r = left+1

            while r<=right:
                if num[r] < num[left]:
                    l+=1
                    num[l], num[r] = num[r], num[l]
                r+=1
            num[left], num[l] = num[l], num[left]
            qs(num, left, l-1)
            qs(num, l+1, right)
        
        qs(nums, 0, len(nums)-1)
        return nums
        