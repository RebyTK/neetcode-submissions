class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1 , cnt2 = 0, 0
        el1 , el2 = float('-inf'), float('-inf')

        for num in nums:
            if cnt1==0 and el2!=num:
                cnt1 = 1
                el1 = num
            elif cnt2 ==0 and el1 != num:
                cnt2 = 1
                el2 = num
            elif num == el1:
                cnt1 +=1
            elif num == el2:
                cnt2 +=1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 , cnt2 = 0, 0
        for num in nums:
            if el1==num:
                cnt1 +=1
            if el2==num: 
                cnt2 +=1
        ans = []
        mini = (n // 3) + 1
        if cnt1 >= mini:
            ans.append(el1)
        if cnt2 >= mini and el2 != el1:
            ans.append(el2)
        return ans

        