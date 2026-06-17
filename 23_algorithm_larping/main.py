def free_time(busy: list[list[int]], work_start: int, work_stop: int) -> list[list[int]]:
    if len(busy) == 0:
        return [[work_start, work_stop]]

    s_busy = sorted(busy, key=lambda x:x[0])
    m_busy = [s_busy[0]]

    for interval in s_busy:
        start, stop = interval
        previous = m_busy[-1]
        p_start, p_stop = previous
        if start <= p_stop:
            m_busy[-1][1] = max(stop, p_stop)
        else:
            m_busy.append(interval)
    
    solution: list[list[int]] = []
    g_start = m_busy[0][0]
    g_stop = m_busy[-1][1]
    if g_start > work_start:
        solution.append([work_start, g_start])

    if len(m_busy) > 1:
        for i, interval in enumerate(m_busy[1:]):
            previous = m_busy[i]
            solution.append([previous[1], interval[0]])

    if g_stop < work_stop:
        solution.append([g_stop, work_stop])

    return solution

if __name__ == "__main__":
    test_cases = (
        ([[9,10],[12,14],[16,17]], 9, 18),
        ([[9,18]], 9, 18),
        ([], 9, 17),
        ([[10,11]], 9, 17)
    )
    test_solution = (
        [[10,12],[14,16],[17,18]],
        [],
        [[9,17]],
        [[9,10],[11,17]]
    )

    for case, solution in zip(test_cases, test_solution):
        test = free_time(*case)
        if test == solution:
            print("Test successful")
        else:
            print(f"Expected : {solution}, got : {test}")