## Problem Statement

Given a person's busy schedule as a list of intervals and their working hours [work_start, work_end], return a list of free time slots within those working hours.

 

**Input:**

- busy: list of busy intervals [[start1, end1], ...] (may be unsorted, may overlap)

- work_start: start of the working day

- work_end: end of the working day

 

**Output:** A list of free intervals within working hours

 

**Examples:**

- busy=[[9,10],[12,14],[16,17]], work_start=9, work_end=18 → [[10,12],[14,16],[17,18]]

- busy=[[9,18]], work_start=9, work_end=18 → [] (completely busy)

- busy=[], work_start=9, work_end=17 → [[9,17]] (completely free)

- busy=[[10,11]], work_start=9, work_end=17 → [[9,10],[11,17]]

 

**Constraints:**

- Busy intervals are guaranteed to be within working hours - Busy intervals may be unsorted and may overlap each other - The result should contain no zero-length intervals


