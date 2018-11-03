# Created by Young Chen at 8/30/2018
class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A)==1:
            return 0
        A.sort()
        first_max=A[0]
        first_min=A[len(A)-1]
        if (first_max-first_min-2*K)>0:
            diff=(first_max-first_min-2*K)
        else:
            diff=0
        return diff

so=Solution()
