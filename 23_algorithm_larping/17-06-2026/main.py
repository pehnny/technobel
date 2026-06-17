class Solution(object):
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals

        solution: list[list[int]] = [] 
        n_start, n_stop = newInterval
        for i, interval in enumerate(intervals):
            start, stop = interval
            if n_start > stop:
                solution.append(interval)
            else:
                if n_stop < start:
                    solution.append([n_start, n_stop])
                    return solution + intervals[i:]
                else:
                    n_stop = max(n_stop, stop)
                    n_start = min(n_start, start)

        if [n_start, n_stop] not in solution:
            solution.append([n_start, n_stop])
        return solution