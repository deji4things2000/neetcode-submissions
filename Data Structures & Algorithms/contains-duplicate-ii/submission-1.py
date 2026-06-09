class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            j=i+1
            while j<n:
                if nums[i] == nums[j] and abs(i-j) <=k:
                    return True
                else:
                    j+=1
        return False