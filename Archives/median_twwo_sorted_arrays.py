class Solution:
    def find_median_optimized(self,nums1, nums2):
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            return (
                self.find_kth(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2)) +
                self.find_kth((total_len // 2) - 1, nums1, 0, len(nums1), nums2, 0, len(nums2))
            ) / 2
        return self.find_kth(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2))

    def find_kth(self,k, nums1, start1, end1, nums2, start2, end2):
        if end1 <= start1:
            return nums2[start2 + k]
        if end2 <= start2:
            return nums1[start1 + k]
    
        mid1 = start1 + (end1 - start1) // 2
        mid2 = start2 + (end2 - start2) // 2
        if k > (mid1 - start1) + (mid2 - start2):
            if nums1[mid1] > nums2[mid2]:
                return self.find_kth(k - (mid2 - start2) - 1, nums1, start1, end1, nums2, mid2 + 1, end2)
            else:
                return self.find_kth(k - (mid1 - start1) - 1, nums1, mid1 + 1, end1, nums2, start2, end2)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.find_kth(k, nums1, start1, mid1, nums2, start2, end2)
            else:
                return self.find_kth(k, nums1, start1, end1, nums2, start2, mid2)

    def findMedianSortedArrays(self, A, B):
        return self.find_median_optimized(A,B)

s = Solution()
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
A = A[1:A[0]+1] 
B = B[1:B[0]+1]
print(s.findMedianSortedArrays(A,B))