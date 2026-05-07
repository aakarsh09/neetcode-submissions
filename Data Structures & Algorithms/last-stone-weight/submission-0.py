class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-x for x in stones]
        heapq.heapify(arr)
        while len(arr)>=2:
                first = heapq.heappop(arr)
                second = heapq.heappop(arr)
                val = abs(first-second)
                heapq.heappush(arr,-val)
        return -arr[0]
