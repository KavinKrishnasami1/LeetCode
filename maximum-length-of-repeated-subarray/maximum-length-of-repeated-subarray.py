class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return len(nums1)
        matrix = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    matrix[i][j] = matrix[i + 1][j + 1] + 1
        return max(max(row) for row in matrix)