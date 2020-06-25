class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        notDupes = set()
        
        for i in nums:
            if i in notDupes:
                return i
            else:
                notDupes.add(i)