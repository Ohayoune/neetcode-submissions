class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Convert the list into a hashset
        numSet = set(nums)
        maxCount = 0
        while numSet:
            
            n = numSet.pop()
            count=1
            while (n-count) in numSet:
                numSet.remove(n-count)
                count+=1
            upCount = 1
            while (n+upCount) in numSet:
                numSet.remove(n+upCount)
                upCount+=1
            maxCount = max(maxCount, upCount + count-1)




        return maxCount
            