def meeting_rooms_conflict(meetings: list[list[int]]) -> bool:
    if len(meetings) < 2:
        return False
    
    sorted_meetings = sorted(meetings, key=lambda m:m[0])
    left = 0
    for right in range(1, len(sorted_meetings)):
        stop = sorted_meetings[left][1]
        start = sorted_meetings[right][0]
        if stop > start:
            return True
        left += 1
    return False
