# 229. Majority Element II

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cad1 = cad2 = None
        cnt1 = cnt2 = 0
        for n in nums:
            if n == cad1:
                cnt1 += 1
            elif n == cad2:
                cnt2 += 1
            elif cnt1 == 0:
                cad1 = n
                cnt1 = 1
            elif cnt2 == 0:
                cad2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
    
        cnt1 = cnt2 = 0
        for n in nums:
            if n == cad1:
                cnt1 += 1
            elif n == cad2:
                cnt2 += 1
        ans = []
        if cnt1 > len(nums)//3:
            ans.append(cad1)
        if cnt2 > len(nums)//3:
            ans.append(cad2)
        return ans

        
            
        
            
            


        