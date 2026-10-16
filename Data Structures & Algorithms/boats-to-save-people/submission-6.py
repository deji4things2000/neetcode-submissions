class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = people
        nums.sort()
        n = len(nums)
        i, j = 0, n-1
        boat = 0
        
        while i<=j:
            suma = nums[i] + nums[j]

            if suma <= limit:
                boat+=1
                i+=1
                j-=1
            else:
                j-=1
                boat+=1
        return boat

            
