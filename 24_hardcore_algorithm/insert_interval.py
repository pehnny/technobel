def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    if len(intervals) == 0:
        return [new_interval]
    if len(new_interval) == 0:
        return intervals

    solution: list[list[int]] = []

    i = 0
    state = new_interval.copy()
    interval = intervals[0]
    start, stop = interval
    while stop < state[0]:
        solution.append(intervals[i])
        i += 1
        if i == len(intervals):
            return solution + [state]
        interval = intervals[i]
        start, stop = interval
    while start <= state[1]:
        state = [min(start, state[0]), max(stop, state[1])]
        i += 1
        if i == len(intervals):
            return solution + [state]
        interval = intervals[i]
        start, stop = interval
    return solution + [state] + intervals[i:]
