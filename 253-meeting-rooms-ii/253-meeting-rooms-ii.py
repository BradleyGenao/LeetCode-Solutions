class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()
        pq = [intervals[0][1]]
        
        for start, end in intervals[1:]:
            if pq[0] > start:
                heapq.heappush(pq, end)
            else:
                heapq.heappushpop(pq, end)
        return len(pq)
        