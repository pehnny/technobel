def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) < 2:
        return intervals
    
    sorted_intervals = sorted(intervals, key=lambda i:i[0])
    solution = [sorted_intervals[0]]
    for interval in sorted_intervals[1:]:
        start, stop = interval
        if start <= solution[-1][1]:
            solution[-1][1] = max(solution[-1][1], stop)
        else:
            solution.append(interval)
    return solution

