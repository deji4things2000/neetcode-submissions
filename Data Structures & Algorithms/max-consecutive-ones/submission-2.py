class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        conS = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                conS=0
            else:
                conS+=1
                maxi = max(maxi, conS)
        return maxi
            