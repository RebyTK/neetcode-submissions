class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cutoff = n//2

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i]==nums[j]:
                    count+=1
            
            if count>cutoff:
                return nums[i]
        return -1