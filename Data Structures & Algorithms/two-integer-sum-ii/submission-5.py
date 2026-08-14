class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        n = len(nums)
        i, j = 0, n-1

        while i<=j:
            suma = nums[i] + nums[j]

            if suma == target:
                return [i+1,j+1]
            elif suma < target:
                i+=1
            else:
                j-=1
        

        