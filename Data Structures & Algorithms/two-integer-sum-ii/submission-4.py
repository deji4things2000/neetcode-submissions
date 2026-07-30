class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1

        while i<j:
            suma = numbers[i] + numbers[j]
            if suma == target:
                return [i+1,j+1]
            elif suma < target:
                i+=1
            else:
                j-=1
        