class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        join = nums1 + nums2
        join.sort()
        if len(join) % 2 != 0:
            return join[int(len(join) / 2)]
        med = (join[int(len(join) / 2)] + join[int((len(join) / 2)) - 1]) / 2
        return med