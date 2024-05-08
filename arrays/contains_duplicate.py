class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        for i in range(len(nums)-1):
            if sorted_nums[i+1]== sorted_nums[i]:
                return True
        return False
