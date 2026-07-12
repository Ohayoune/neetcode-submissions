class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashset to check potential nums
        check_Set = set()
        for check_Num in nums:
            if check_Num in check_Set:
                return True
            check_Set.add(check_Num)
        return False


        