# Created by Young Chen at 8/26/2018
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n==0 :return []
        for i in range(n):
            num = nums[i]
            while num != -1:
                tmp = nums[num-1]
                nums[num-1] = -1
                num = tmp
        return [i+1 for i in range(n) if nums[i]!=-1]