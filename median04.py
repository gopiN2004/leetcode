class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     arr=nums1+nums2
     n=len(arr)
     arr.sort()
     if n%2==1:
        return round(float(arr[n//2]),4)
     else:
        return round(float((arr[(n//2)-1] +arr[n//2])/2 ),4)