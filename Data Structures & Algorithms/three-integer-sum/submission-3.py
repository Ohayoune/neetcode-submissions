class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = [[]]
        ansSet = set()
        ans.pop()

        for beg in range(len(nums)-2):
            l = beg + 1
            r = len(nums) - 1
            while l < r:
                comb = nums[l] + nums[r] + nums[beg]
                if comb == 0:
                    foundLis = [nums[beg],nums[l],nums[r]]
                    foundTuple = tuple(foundLis)
                    if(foundTuple not in ansSet):
                        ansSet.add(foundTuple)
                        ans.append(foundLis)
                    l+=1
                    r-=1
                elif comb > 0:
                    r-=1
                else:
                    l += 1
        
        return ans
        #map of all the possible additions