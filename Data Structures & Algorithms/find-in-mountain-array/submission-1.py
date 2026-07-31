class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        i, j = 0, n-1

        #Find Peak

        while i<j:
            mid = (i+j)//2

            if mountainArr.get(mid) < mountainArr.get(mid+1):
                i = mid + 1
            else:
                j = mid 
        peak = i

        #search Left

        i, j = 0, peak

        while i<=j:
            mid = (i+j)//2

            val = mountainArr.get(mid)
            if val ==target:
                return mid

            elif val < target:
                i = mid + 1
            else:
                j = mid - 1
            
        #search right

        i, j = peak+1, n-1

        while i<=j:
            mid = (i+j)//2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val<target:
                j = mid - 1
            else:
                i = mid + 1
        
        return -1
        