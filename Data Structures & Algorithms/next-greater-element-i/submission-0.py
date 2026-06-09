class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for x in nums1:
            pos = nums2.index(x)
            nt = -1

            for j in range(pos+1, len(nums2)):
                if nums2[j] > x:
                    nt = nums2[j]
                    break
            res.append(nt)
        return res





