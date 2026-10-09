class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #In python, ints can have arbitrary precision, so long works
        array_sum = 1
        empty_nums = []
        
        for i in range(len(nums)):
            if(nums[i] == 0):
                empty_nums.append(i)
            else:
                array_sum = array_sum * nums[i]
        if len(empty_nums) > 0:
            for i in range(len(nums)):
                nums[i] = 0
            if len(empty_nums) == 1:
                nums[empty_nums[0]] = array_sum
            return nums
        

        for i in range(len(nums)):
            nums[i] = array_sum//nums[i]
        #Since i is already in the array_sum product, we won't get a decimal.
        return nums