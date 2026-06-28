import heapq
def minimum_number_of_meeting_rooms(meetings: list[list[int]]) -> int:
    if len(meetings) == 0:
        return 0
    if len(meetings) == 1:
        return 1
    
    max_rooms = 1
    sorted_meetings = sorted(meetings, key=lambda m:m[0])
    stack: list[int] = []
    for meeting in sorted_meetings:
        start, stop = meeting
        heapq.heappush(stack, stop)
        while stack[0] <= start:
            heapq.heappop(stack)
        max_rooms = max(max_rooms, len(stack))
    return max_rooms
