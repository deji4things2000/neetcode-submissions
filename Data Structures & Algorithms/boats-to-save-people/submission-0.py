class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats  = 0
        people.sort()
        n = len(people)

        i, j = 0, n-1

        while i<=j:
            if people[i] + people[j] <=limit:
                i+=1
            j-=1 #Always take the heaviest person
            boats+=1
        return boats

        