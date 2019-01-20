class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numTot = nums1 + nums2
        numTot.sort()
        if len(numTot) % 2.0 == 0:
            return (numTot[len(numTot)/2]+numTot[(len(numTot)/2)-1])/2.0
        else:
            return numTot[len(numTot)/2]q
