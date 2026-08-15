class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = people
        nums.sort()
        n = len(nums)
        boat=0
        i,j = 0, n-1

        while i<=j:
            suma = nums[i] + nums[j]

            if suma <= limit:
                i+=1
                j-=1
            elif suma > limit:
                j-=1
            boat+=1
        return boat

        