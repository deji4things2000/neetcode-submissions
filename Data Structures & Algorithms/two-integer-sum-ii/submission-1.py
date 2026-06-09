class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=numbers
        l,r = 0, len(numbers)-1
        res=[]
        while l<r:
            diff=target-n[r]

            if n[l]==diff:
                return [l+1,r+1]
            elif n[l]>diff:
                r-=1
            else:
                l+=1
        return []



