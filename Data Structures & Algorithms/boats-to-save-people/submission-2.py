class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n-1
        boat = 0
        nums = people

        while i<=j:
            suma = nums[i] + nums[j]

            if suma <= limit:
                boat+=1
                i+=1
                j-=1
            elif suma > limit:
                j-=1
                boat+=1
            else:
                i-=1
        return boat
            
