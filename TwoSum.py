class Solution:
    def twoSum(self, nums, target):
       d={}
       for i,n in enumerate(nums):
            g=target-n
            if g in d:
                return[d[g],i]
            else:
                d[n]=i
                
c=Solution()
c.twoSum([2,7,11,15],9)