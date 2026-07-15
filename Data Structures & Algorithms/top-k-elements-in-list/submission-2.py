class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Use a dict to get a list of the frequency of each value
        my_Dict = dict()
        for n in nums:
            if n in my_Dict:
                my_Dict[n] += 1
            else:
                my_Dict[n] = 1
        heap = []
        lis = list(my_Dict.items())
        for i in lis:
            heapq.heappush(heap, (i[1], i[0]))
        while len(heap) > k:
            heapq.heappop(heap)
        lis2 = []
        for i in heap:
            
            lis2.append(i[1])

        return lis2