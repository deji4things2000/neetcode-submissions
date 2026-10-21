class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        i,j = 0, m

        while i<=j:
            part1 = (i+j)//2
            part2 = ((m+n+1)//2) - part1

            left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            right1 = float('inf') if part1 == m else nums1[part1]

            left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            right2 = float('inf') if part2 == n else nums2[part2]

            if left1<=right2 and left2<=right1:
                if (m+n)%2:
                    return max(left1, left2)
                
                return (max(left1, left2)+ min(right1, right2))/2

            elif left1 > right2:
                j = part1 - 1
            else:
                i = part1 + 1

        