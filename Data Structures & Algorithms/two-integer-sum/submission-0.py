class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp={}

        n =len(nums)

        for i in range(n):
            num = nums[i]
            req = target-num

            if req in mpp:
                return[mpp[req],i]
            mpp[num] = i
        return [-1,-1]
        