class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        length = r+1-l

        while length > 0:
            mid = l+int(length/2)
            if nums[mid]  == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
            
            length = r+1-l



        return -1