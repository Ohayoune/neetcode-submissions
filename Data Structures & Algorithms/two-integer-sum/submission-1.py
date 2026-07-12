class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        md = dict()
        for index, value in enumerate(nums): 
            if (target-value) in md:
                return [md.get(target-value), index]
            else:
                md[value] = index
        return [-1,-1] #error, if the function fails