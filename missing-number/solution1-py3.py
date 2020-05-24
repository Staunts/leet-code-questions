class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        size = len(nums) + 1
        
        desired = [i for i in range(0, size)]
        
        for idx, val in enumerate(nums):
            desired.remove(val)
            
        return desired[0]