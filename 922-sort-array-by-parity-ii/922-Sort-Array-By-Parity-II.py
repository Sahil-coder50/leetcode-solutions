class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        
        even_ptr = 0
        odd_ptr = 1

        n = len(nums)

        while even_ptr<n and odd_ptr<n:

            if (nums[even_ptr] & 1) == 0:
                even_ptr+=2
            elif (nums[odd_ptr] & 1) !=0:
                odd_ptr+=2
            else:
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
                even_ptr+=2
                odd_ptr+=2
        
        return nums

        
        return nums
        
        return nums
